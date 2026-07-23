<div align="center">

  <!-- TOP HEADER BANNER -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0053db,100:10141d&height=280&section=header&text=🎫%20Support%20CRM%20—%20Command%20Center&fontSize=42&fontColor=ffffff&fontAlignY=42&animation=twinkling" width="100%" />

  <br />

  <!-- HERO GRAPHIC -->
  <img src="./Frontend/gifs/test5.gif" width="600px" style="image-rendering: pixelated;" />

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

### 📊 Repository Analytics & Performance Metrics

<div align="center">

  <!-- REPO METRICS & LANGUAGE CARDS -->
  <a href="https://github.com/sahilsakure/Datastraw_Suppor_CRM">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=sahilsakure&repo=Datastraw_Suppor_CRM&theme=tokyonight&show_owner=true" height="150" />
  </a>
  <a href="https://github.com/sahilsakure/Datastraw_Suppor_CRM">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sahilsakure&repo=Datastraw_Suppor_CRM&layout=compact&theme=tokyonight&hide=html,css" height="150" />
  </a>

  <br /><br />

  <!-- PERFORMANCE METRICS TABLE -->
  <table>
    <tr>
      <td align="center"><b>⚡ Avg Response Time</b><br /><code>&lt; 15ms (FastAPI)</code></td>
      <td align="center"><b>🎟️ Ticket Handling</b><br /><code>Real-Time Search & Filter</code></td>
      <td align="center"><b>🗄️ Database Querying</b><br /><code>Async SQLite CRUD</code></td>
      <td align="center"><b>🎨 UI Theme</b><br /><code>Tailwind Dynamic Dark/Light</code></td>
    </tr>
  </table>

</div>

---

### 📸 Interface Showcase

<div align="center">

  #### 🖥️ Main Dashboard — Ticket Command Center
  *Real-time ticket monitoring, live status indicators, and global search.*
  <br /><br />
  <img src="./Frontend/images/dashboard.png" width="90%" alt="Support CRM Dashboard View" />

  <br /><br /><br />

  #### 📝 Ticket Management & Internal Notes
  *Detailed ticket inspect view with real-time audit trail and staff notes.*
  <br /><br />
  <img src="./Frontend/images/ticket-details.png" width="90%" alt="Ticket Details View" />

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