# Smart Task Manager
A full-stack Flask application featuring persistent storage, user authentication, and an automated task prioritization engine.

## Key Features
* **User Authentication:** Secure signup/login system using session-based management and SHA-256 password hashing.
* **Persistent Storage:** SQLite3 backend with relational table mapping (Users ↔ Tasks).
* **"Smart" Priority Engine:** Logic-driven task sorting that automatically calculates "days remaining" and flags overdue/upcoming items based on real-time server dates.
* **RESTful Routing:** Implementation of CRUD (Create, Read, Update, Delete) operations via Flask.

## Tech Stack
* **Backend:** Python (Flask)
* **Database:** SQLite3
* **Logic:** Python `datetime` & `hashlib`

## Self-Directed Learning Goals
This project marks my transition from Object-Oriented Console Applications to Web Architecture. Key learning milestones included:
* **State Management:** Moving from local variables to persistent SQL databases.
* **Web Security:** Implementing password hashing and learning the importance of protecting user data.
* **Environment Design:** Managing server-side logic vs. client-side requests.

## How to Run
1. Clone the repo: `git clone https://github.com/steveBuelow/SmartProductivityManager.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python smart-task-manager.py`

##  API & Usage
Navigation is currently handled via URL parameters. While the server is running locally (usually on `http://127.0.0.1:5000`), use the following routes:

* **Authentication:**
  * `/signup?username=steve&password=123` — Register a new account.
  * `/login?username=steve&password=123` — Start a session.
  * `/logout` — End your session.
* **Task Management:**
  * `/tasks` — View your personalized "Smart" task list.
  * `/add-task?title=Finish+Project&date=2026-05-01` — Add a new task (use YYYY-MM-DD format).
  * `/remove-task?id=1` — Delete a task by its unique ID.

## Roadmap (v2.0)
* Refactor authentication to use `POST` requests and HTML forms to secure credentials in transit.
* Implement Jinja2 templating for a structured UI.


