<div align="center">

  <!-- TOP HEADER BANNER -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0053db,100:10141d&height=280&section=header&text=🎫%20Support%20CRM%20—%20Command%20Center&fontSize=42&fontColor=ffffff&fontAlignY=42&animation=twinkling" width="100%" />

  <br />

  <!-- LOCAL HALFTONE GIF ANIMATION -->
  <img src="./Frontend/gifs/efecto-recording.gif" width="260px" />

  <br /><br />

  <!-- DYNAMIC BADGES -->
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
    <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
    <img src="https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  </p>

  <br />

  <!-- TYPING ANIMATION BANNER -->
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=24&pause=1000&color=3D8BFF&width=700&lines=Enterprise+Customer+Support+Management;Real-Time+Ticket+Tracking+%26+Filtering;Asynchronous+FastAPI+%2B+SQLite+Architecture" alt="Typing SVG" />

</div>

---

### 🚀 Overview

**Support CRM** is a high-performance customer support management system built with an asynchronous **FastAPI** backend, **SQLite** relational database, and an ultra-responsive, dark-mode compatible **Tailwind CSS** UI.

It provides support engineering teams with an intuitive **Ticket Command Center** to create, search, filter, track, and annotate customer support tickets in real time.

---

### ✨ Features

- 🎟️ **Ticket Management:** Create, track, and update ticket statuses (`Open`, `Pending`, `Resolved`, `Closed`).
- 📝 **Internal Activity & Notes:** Append team notes and system updates to individual support threads.
- 🔍 **Real-Time Filtering & Search:** Instantly query tickets by customer name, email, subject, or ticket ID.
- 📖 **Embedded Knowledge Base:** In-app documentation and troubleshooting guides for support operators.
- 🌓 **Dynamic Theme System:** Built-in Light and Dark Mode toggle.
- ⚡ **Auto-Seeding Database:** Automatically initializes relational schema and sample seed data on first boot.

---

### 🛠️ Tech Stack & Capabilities

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,sqlite,tailwind,html,css,js,git,github,vscode&perline=10" />
</div>

---

### 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/tickets` | Create a new support ticket |
| `GET` | `/api/tickets` | Retrieve all tickets (supports `status` filter & `search` query) |
| `GET` | `/api/tickets/{ticket_id}` | Retrieve ticket details along with internal notes history |
| `PUT` | `/api/tickets/{ticket_id}` | Update ticket status or customer information |
| `POST` | `/api/tickets/{ticket_id}/notes` | Add an internal note to a ticket thread |

---

### 💻 System Architecture & Setup

```bash
# 1. Clone the repository
git clone [https://github.com/sahilsakure/Datastraw_Suppor_CRM.git](https://github.com/sahilsakure/Datastraw_Suppor_CRM.git)
cd Datastraw_Suppor_CRM

# 2. Set up virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows

# 3. Install dependencies & Run server
pip install -r Backend/requirements.txt
cd Backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000