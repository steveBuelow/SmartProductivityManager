# Smart Productivity Manager
A Full-Stack Flask application featuring a SQLite backend, user authentication, and a dynamic JavaScript frontend.

Built to bridge the gap between backend logic and interactive web interfaces, focusing on state management and secure data handling.

## 🚀 Recent Updates (Current State)
* **Decoupled Frontend:** Implemented a single-page interface using HTML5, CSS3, and Vanilla JavaScript.
* **Asynchronous Communication:** Replaced URL-based inputs with `fetch()` API calls (AJAX), allowing the app to update without refreshing the page.
* **Enhanced Security:** Transitioned from `GET` to `POST` requests for authentication and task creation, ensuring credentials are not exposed in the browser history.
* **DOM Manipulation:** Dynamic task rendering with a "Smart" prioritization display.

## Key Features
* **User Authentication:** Session-based login system with password hashing (implemented for educational purposes to understand the request-lifecycle).
* **Persistent Storage:** SQLite3 backend managing relational data between users and tasks.
* **Dynamic Task Management:** Real-time adding and deleting of tasks with integrated due-date tracking.
* **Clean Architecture:** Separated concerns between `app.py` (entry), `routes.py` (API), and `templates/` (UI).

## Tech Stack
* **Backend:** Python (Flask)
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Version Control:** Git

## Project Structure
* **app.py:** Initializes the Flask environment.
* **routes.py:** The API layer handling JSON requests and session management.
* **templates/index.html:** The single-page frontend (HTML/CSS/JS).
* **db.py / models.py:** Database schema and logic.

## How to Run
1. **Clone the repo:**
    ```bash
   git clone [https://github.com/steveBuelow/SmartProductivityManager.git](https://github.com/steveBuelow/SmartProductivityManager.git)
   cd SmartProductivityManager
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    python app.py
    ```
4.  **Access the UI:**
    Open your browser to `http://127.0.0.1:5000/`

## API Reference
While the UI handles most interactions, the backend provides the following JSON endpoints:
* `POST /signup` - Creates a new user.
* `POST /login` - Authenticates user and starts session.
* `GET /tasks` - Retrieves JSON list of tasks for the logged-in user.
* `POST /add-task` - Accepts task title and due date.
* `DELETE /remove-task` - Deletes a specific task via ID.

## Self-Directed Learning Goals
This project marks my transition from console applications to **Full-Stack Web Architecture**. Key milestones:
* **The Request/Response Cycle:** Understanding how the browser communicates with a Python server via JSON.
* **Frontend-Backend Integration:** Learning to manipulate the DOM (Document Object Model) based on server data.
* **State Management:** Handling user sessions across different routes.
