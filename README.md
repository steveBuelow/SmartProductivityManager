# Smart Task Manager
A Flask + SQLite backend app with authentication and a rule-based task prioritization engine.

Built to simulate real-world backend concerns like persistence, auth, and time-based logic.

## Key Features
* **User Authentication:** Basic authentication system using SHA-256 hashing (for learning purposes; not production-grade authentication)
* **Persistent Storage:** SQLite3 backend with relational table mapping (Users ↔ Tasks).
* **"Smart" Priority Engine:** Rule-based task sorting that calculates "days remaining" and flags overdue/upcoming items using server-side date logic.
* **Routing & CRUD:** Implementation of Create, Read, Update, Delete operations via Flask routes.

## Project Structure
* **app.py:** The entry point that initializes the Flask server and registers routes.
* **routes.py:** Contains all URL endpoints and request handling logic.
* **models.py:** Handles data processing, password hashing, and database queries.
* **db.py:** Manages the SQLite connection and schema initialization.
* **.gitignore:** Ensures sensitive files like the database and environment junk aren't tracked.

## Tech Stack
* **Backend:** Python (Flask)
* **Database:** SQLite3
* **Logic:** Python `datetime` & `hashlib`
* **Version Control:** Git 

## Self-Directed Learning Goals
This project marks my transition from Object-Oriented Console Applications to Web Architecture. Key learning milestones included:
* **State Management:** Moving from local variables to persistent SQL databases.
* **Web Security:** Implementing password hashing and learning the importance of protecting user data.
* **Backend Architecture:** Structuring server-side logic and handling HTTP requests within a Flask application.

## How to Run
1. Clone the repo: `git clone https://github.com/steveBuelow/SmartProductivityManager.git`
`cd SmartProductivityManager`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

##  Routes / Usage
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


