import sqlite3
import os
from datetime import datetime, timedelta

DATABASE_FILE = "support_crm.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tickets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id TEXT UNIQUE NOT NULL,
        customer_name TEXT NOT NULL,
        customer_email TEXT NOT NULL,
        subject TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Open',
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)
    
    # Create notes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id TEXT NOT NULL,
        note_text TEXT NOT NULL,
        created_at TEXT NOT NULL,
        FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id) ON DELETE CASCADE
    )
    """)
    
    conn.commit()
    
    # Check if we need to seed data
    cursor.execute("SELECT COUNT(*) FROM tickets")
    if cursor.fetchone()[0] == 0:
        seed_data(conn)
        
    conn.close()

def seed_data(conn):
    cursor = conn.cursor()
    now = datetime.utcnow()
    
    # Define sample tickets
    tickets = [
        {
            "ticket_id": "TKT-001",
            "customer_name": "John Doe",
            "customer_email": "john.doe@gmail.com",
            "subject": "API Authentication Failure on v2.1",
            "description": "Hello, I am getting a 401 Unauthorized error when attempting to access the v2.1 endpoints of the API, even though my token is active and valid. Please check if there is an issue with the auth validation service.",
            "status": "Open",
            "created_at": (now - timedelta(hours=2)).isoformat() + "Z",
            "updated_at": (now - timedelta(hours=2)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-002",
            "customer_name": "Maria Bosch",
            "customer_email": "maria.b@company.com",
            "subject": "Billing inquiry regarding subscription upgrade",
            "description": "Hi team, I tried upgrading our account to the Enterprise tier but was charged twice. Also, the invoice shows the wrong billing address. Please refund the duplicate charge and correct the billing address on INV-2026-042.",
            "status": "Pending",
            "created_at": (now - timedelta(hours=5)).isoformat() + "Z",
            "updated_at": (now - timedelta(hours=5)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-003",
            "customer_name": "Liam White",
            "customer_email": "liam.white@outlook.com",
            "subject": "UI Glitch on Dashboard mobile view",
            "description": "On my iPhone 14 Pro, the main navigation sidebar overlaps with the statistics cards in portrait orientation. It makes it hard to tap on the dashboard links. Works fine on desktop.",
            "status": "Closed",
            "created_at": (now - timedelta(days=1)).isoformat() + "Z",
            "updated_at": (now - timedelta(days=1)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-004",
            "customer_name": "Sam Knight",
            "customer_email": "sam.k@knightcorp.com",
            "subject": "New feature request: Dark mode toggles",
            "description": "It would be super helpful to have a Dark Mode toggle in the support panel. Working late night support shifts makes the bright white background very straining on the eyes.",
            "status": "Open",
            "created_at": (now - timedelta(days=1, hours=3)).isoformat() + "Z",
            "updated_at": (now - timedelta(days=1, hours=3)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-005",
            "customer_name": "Aria Tan",
            "customer_email": "aria.tan@startup.io",
            "subject": "Password reset link not working",
            "description": "The password reset email arrives, but clicking the link redirects me to a 404 page instead of the password reset form. I tried it twice with the same result.",
            "status": "Closed",
            "created_at": (now - timedelta(days=2)).isoformat() + "Z",
            "updated_at": (now - timedelta(days=2)).isoformat() + "Z"
        }
    ]
    
    # Insert tickets
    for t in tickets:
        cursor.execute("""
        INSERT INTO tickets (ticket_id, customer_name, customer_email, subject, description, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            t["ticket_id"],
            t["customer_name"],
            t["customer_email"],
            t["subject"],
            t["description"],
            t["status"],
            t["created_at"],
            t["updated_at"]
        ))
    
    # Define sample notes
    notes = [
        {
            "ticket_id": "TKT-002",
            "note_text": "James Wilson (Lead Agent): I've verified the transaction on Stripe. It looks like a legacy tier was accidentally triggered during the last database migration. I'm waiting for Billing Dept to confirm the refund capability.",
            "created_at": (now - timedelta(minutes=45)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-001",
            "note_text": "System: Ticket automatically created from customer portal submission.",
            "created_at": (now - timedelta(hours=2)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-003",
            "note_text": "Alex Rivera: Confirmed the mobile layout issues on iOS Safari. Opened a bug ticket in Jira for the frontend team to fix the CSS layout parameters.",
            "created_at": (now - timedelta(hours=18)).isoformat() + "Z"
        },
        {
            "ticket_id": "TKT-003",
            "note_text": "System: Status updated to Closed. Resolution: Fixed by CSS update deployment in v2.1.4.",
            "created_at": (now - timedelta(hours=2)).isoformat() + "Z"
        }
    ]
    
    # Insert notes
    for n in notes:
        cursor.execute("""
        INSERT INTO notes (ticket_id, note_text, created_at)
        VALUES (?, ?, ?)
        """, (
            n["ticket_id"],
            n["note_text"],
            n["created_at"]
        ))
        
    conn.commit()
    print("Database successfully seeded with sample data.")

if __name__ == "__main__":
    init_db()
