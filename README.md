

# LokSetu – AI-Assisted Grievance Redressal Platform

LokSetu is a **full-stack web application** designed to streamline grievance submission, verification, and resolution using **secure authentication**, **role-based dashboards**, and **AI assistance**.
It bridges the gap between **citizens and authorities** by ensuring transparency, accountability, and faster resolutions.

---

## Problem Statement

Existing grievance redressal systems face critical challenges:

* Fake or unverifiable complaints
* Lack of real-time tracking for citizens
* Manual overload for authorities
* Poor transparency and accountability

These issues lead to delayed resolutions and reduced public trust.

---

## Solution – LokSetu

LokSetu provides a **secure, scalable, and intelligent grievance platform** where:

* Citizens can submit grievances with proof
* Authorities can review, verify, and resolve complaints efficiently
* AI assists in identifying suspicious or valid submissions
* Real-time status tracking ensures transparency

---

##  Key Features

###  Citizen Module

* Secure registration & login (JWT based)
* Submit grievances with description and proof
* Track grievance status in real time

###  Authority Module

* Role-based authority login
* View all grievances
* Update grievance status (Pending / In-Progress / Resolved)
* Prioritize verified complaints

###  Authentication & Security

* JWT-based authentication
* Role-based access control
* Secure password hashing (bcrypt)

###  AI Assistance (MVP Scope)

* Proof verification support
* Fake / suspicious complaint flagging
* Reduces manual workload for authorities

---

## 🛠️ Tech Stack

### Backend

* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **JWT Authentication**
* **Passlib (bcrypt)**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript (Vanilla JS)**

### VISUAL OVERVIEW
* SWAGGER UI $ MAIN UI 
* Note: The current UI is intentionally minimal, as the MVP focuses on validating core functionality and backend integration. UI/UX enhancements are planned in future iterations.

![alt text](<Screenshot (18).png>) ![alt text](<Screenshot (19).png>) ![alt text](<Screenshot (20).png>) ![alt text](<Screenshot (21).png>) ![alt text](<Screenshot (22).png>) ![alt text](<Screenshot (24).png>) ![alt text](<Screenshot (25).png>)

### MOCKUP UI ( these are the desired ui!)

![alt text](<screen (7).png>) ![alt text](<screen (6).png>) ![alt text](<screen (5).png>) ![alt text](<screen (4).png>) ![alt text](<screen (3).png>) ![alt text](<screen (2).png>) ![alt text](screen.png)


### Tools

* gemini (reasearch)
* stich ai (ui mockups)
* Swagger UI (API testing)
* VS Code
* GitHub

---

## Project Structure(how to run the application)

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger UI:http://127.0.0.1:8000/docs
```

* Open `frontend/index.html` in browser
* Or use VS Code Live Server for better experience

Ensure backend is running on:

```
http://127.0.0.1:8000
```

---

## 🔁 Application Flow

1. User registers/logs in
2. JWT token is generated and stored
3. Citizen submits grievance with proof
4. Authority reviews grievance
5. Status is updated
6. Citizen tracks real-time progress

---

## MVP Scope

 Working authentication
 Database-backed users & complaints
 Role-based dashboards
 Backend-frontend integration
 AI-assisted verification (basic)

---

## Future Enhancements

* Multi-lingual support
* GIS / Map-based grievance tracking
* SMS / Email notifications
* Advanced AI verification models
* Mobile app version
 ---
## Conclusion

LokSetu is not just a prototype — it is a **functional MVP** that demonstrates how technology, AI, and thoughtful design can transform grievance redressal systems.


