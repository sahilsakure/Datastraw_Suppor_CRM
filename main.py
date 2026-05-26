import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import sqlite3

from database import init_db, get_db_connection, DATABASE_FILE

# Initialize Database on Startup
init_db()

app = FastAPI(title="Support CRM Backend", description="FastAPI + SQLite Support CRM Backend")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Schemas
class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str

class TicketUpdate(BaseModel):
    status: str  # 'Open', 'Pending', 'Resolved', 'Closed'
    customer_name: Optional[str] = None
    customer_email: Optional[EmailStr] = None
    subject: Optional[str] = None
    description: Optional[str] = None

class TicketResponse(BaseModel):
    id: int
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    created_at: str
    updated_at: str

class NoteCreate(BaseModel):
    note_text: str

class NoteResponse(BaseModel):
    id: int
    ticket_id: str
    note_text: str
    created_at: str

class TicketDetailResponse(BaseModel):
    ticket: TicketResponse
    notes: List[NoteResponse]

# Helper function to generate ticket IDs like TKT-001
def generate_next_ticket_id(conn) -> str:
    cursor = conn.cursor()
    cursor.execute("SELECT ticket_id FROM tickets ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        last_id = row[0]
        try:
            # Last ID is in TKT-XXX format
            num = int(last_id.split("-")[1])
            next_num = num + 1
        except (IndexError, ValueError):
            next_num = 1
    else:
        next_num = 1
    return f"TKT-{next_num:03d}"

# Serve the main index.html page
@app.get("/")
def get_index():
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Frontend"))
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    # Fallback to dashboard code.html if index.html is not created yet
    fallback_path = os.path.join(frontend_dir, "support_crm_dashboard", "code.html")
    return FileResponse(fallback_path)

# Mount the Frontend directory to serve static assets (like screen.png)
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Frontend"))
app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")

# --- API Endpoints ---

# 1. Create a ticket
@app.post("/api/tickets", response_model=TicketResponse, status_code=201)
def create_ticket(ticket: TicketCreate):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        ticket_id = generate_next_ticket_id(conn)
        now_str = datetime.utcnow().isoformat() + "Z"
        
        cursor.execute("""
        INSERT INTO tickets (ticket_id, customer_name, customer_email, subject, description, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ticket_id,
            ticket.customer_name,
            ticket.customer_email,
            ticket.subject,
            ticket.description,
            "Open",  # Default status
            now_str,
            now_str
        ))
        
        ticket_db_id = cursor.lastrowid
        
        # Add a system note for ticket creation
        cursor.execute("""
        INSERT INTO notes (ticket_id, note_text, created_at)
        VALUES (?, ?, ?)
        """, (
            ticket_id,
            "System: Ticket automatically created.",
            now_str
        ))
        
        conn.commit()
        
        # Fetch the created ticket to return
        cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_db_id,))
        row = cursor.fetchone()
        return dict(row)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# 2. Get all tickets (supports search & status filtering)
@app.get("/api/tickets", response_model=List[TicketResponse])
def get_tickets(
    status: Optional[str] = Query(None, description="Filter by status (Open, Pending, Resolved, Closed)"),
    search: Optional[str] = Query(None, description="Search by subject, customer name, email, or ticket ID")
):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM tickets WHERE 1=1"
    params = []
    
    # Filter by status if it's not None, empty, or "All Statuses"
    if status and status.lower() not in ["all statuses", "all", ""]:
        query += " AND LOWER(status) = LOWER(?)"
        params.append(status)
        
    # Search query
    if search and search.strip():
        search_pattern = f"%{search.strip()}%"
        query += " AND (customer_name LIKE ? OR customer_email LIKE ? OR subject LIKE ? OR ticket_id LIKE ?)"
        params.extend([search_pattern, search_pattern, search_pattern, search_pattern])
        
    query += " ORDER BY id DESC"
    
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")
    finally:
        conn.close()

# 3. Get ticket details with notes
@app.get("/api/tickets/{ticket_id}", response_model=TicketDetailResponse)
def get_ticket_detail(ticket_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Fetch ticket
        cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
        ticket_row = cursor.fetchone()
        if not ticket_row:
            raise HTTPException(status_code=404, detail=f"Ticket {ticket_id} not found")
            
        # Fetch notes
        cursor.execute("SELECT * FROM notes WHERE ticket_id = ? ORDER BY id DESC", (ticket_id,))
        notes_rows = cursor.fetchall()
        
        return {
            "ticket": dict(ticket_row),
            "notes": [dict(n) for n in notes_rows]
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database retrieval error: {str(e)}")
    finally:
        conn.close()

# 4. Update ticket status
@app.put("/api/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: str, ticket_update: TicketUpdate):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        
        # Check if ticket exists
        cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
        existing_ticket = cursor.fetchone()
        if not existing_ticket:
            raise HTTPException(status_code=404, detail=f"Ticket {ticket_id} not found")
            
        existing_ticket_dict = dict(existing_ticket)
        old_status = existing_ticket_dict["status"]
        new_status = ticket_update.status
        
        now_str = datetime.utcnow().isoformat() + "Z"
        
        # Build update query
        update_fields = ["status = ?", "updated_at = ?"]
        params = [new_status, now_str]
        
        if ticket_update.customer_name is not None:
            update_fields.append("customer_name = ?")
            params.append(ticket_update.customer_name)
        if ticket_update.customer_email is not None:
            update_fields.append("customer_email = ?")
            params.append(ticket_update.customer_email)
        if ticket_update.subject is not None:
            update_fields.append("subject = ?")
            params.append(ticket_update.subject)
        if ticket_update.description is not None:
            update_fields.append("description = ?")
            params.append(ticket_update.description)
            
        params.append(ticket_id)
        
        cursor.execute(f"""
        UPDATE tickets 
        SET {', '.join(update_fields)}
        WHERE ticket_id = ?
        """, tuple(params))
        
        # If status changed, record it in a note
        if old_status != new_status:
            system_note = f"System: Ticket status updated from {old_status} to {new_status}."
            cursor.execute("""
            INSERT INTO notes (ticket_id, note_text, created_at)
            VALUES (?, ?, ?)
            """, (ticket_id, system_note, now_str))
            
        conn.commit()
        
        # Get updated ticket
        cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
        row = cursor.fetchone()
        return dict(row)
    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database update error: {str(e)}")
    finally:
        conn.close()

# 5. Add a note to a ticket
@app.post("/api/tickets/{ticket_id}/notes", response_model=NoteResponse, status_code=201)
def add_ticket_note(ticket_id: str, note: NoteCreate):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        
        # Check if ticket exists
        cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail=f"Ticket {ticket_id} not found")
            
        now_str = datetime.utcnow().isoformat() + "Z"
        
        cursor.execute("""
        INSERT INTO notes (ticket_id, note_text, created_at)
        VALUES (?, ?, ?)
        """, (
            ticket_id,
            note.note_text,
            now_str
        ))
        
        note_db_id = cursor.lastrowid
        conn.commit()
        
        cursor.execute("SELECT * FROM notes WHERE id = ?", (note_db_id,))
        row = cursor.fetchone()
        return dict(row)
    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database note error: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    # pyrefly: ignore [missing-import]
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
