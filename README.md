# Smart Productivity Manager

## Preview

### Login

<img width="871" height="382" alt="login-SmartProductivityManager" src="https://github.com/user-attachments/assets/8ba90a3a-f7fb-4f5d-b2f4-5ff9d5bc6a02" />

### Dashboard

<img width="871" height="382" alt="dashboard-SmartProductivityManager" src="https://github.com/user-attachments/assets/932b0ba1-4221-4308-90b8-852acefa78e0" />

A full-stack task management web application built with Flask, SQLite, and vanilla JavaScript.
This project demonstrates backend API design, session-based authentication, persistent storage, and dynamic frontend updates without page refreshes.

Built to bridge the gap between backend logic and interactive web interfaces, focusing on state management and secure data handling.

---

## Overview

Smart Productivity Manager allows users to create an account, log in, and manage tasks through an interactive browser interface.

This project was built to strengthen my understanding of:

* The request/response cycle
* Backend routing and API design
* Persistent data storage with SQLite
* Session-based authentication
* Frontend–backend integration using `fetch()`
* DOM manipulation with vanilla JavaScript

---

## Features

* **User Authentication**
  Session-based login system with password hashing (SHA-256, educational implementation)

* **Persistent Storage**
  SQLite database storing users and tasks with relational structure

* **Task Analytics**  
  Displays simple task completion statistics using aggregated backend data

* **Task Management**
  Add, view, and remove tasks with due dates

* **Dynamic UI**
  Updates tasks in real time using `fetch()` (AJAX) without page reloads

* **Modular Architecture**
  Clean separation between app initialization, routing, models, and database logic

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Version Control:** Git / GitHub

---

## Project Structure

```text
SmartProductivityManager/
├── app.py
├── db.py
├── models.py
├── routes.py
├── requirements.txt
├── templates/
│   └── index.html
└── .gitignore
```

### File Responsibilities

* **`app.py`**
  Initializes the Flask app, registers routes, and defines global error handlers

* **`db.py`**
  Handles database connection and schema initialization

* **`models.py`**
  Contains database logic for users and tasks

* **`routes.py`**
  Defines API endpoints and request handling

* **`templates/index.html`**
  Frontend UI using HTML, CSS, and JavaScript

---

## How It Works

1. User signs up or logs in
2. Frontend sends JSON requests using `fetch()`
3. Flask processes the request and interacts with SQLite
4. JSON response is returned
5. Frontend updates the UI dynamically

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/steveBuelow/SmartProductivityManager.git
cd SmartProductivityManager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## API Endpoints

* `POST /signup` — Create a new user
* `POST /login` — Authenticate user and start session
* `GET /tasks` — Retrieve user tasks
* `POST /add-task` — Add a new task
* `DELETE /remove-task` — Mark task as completed
* `GET /api/stats` — Retrieve task completion stats

---

## Design Decisions

* **Vanilla JavaScript frontend**
  Keeps focus on core concepts like DOM manipulation and API calls

* **SQLite database**
  Lightweight and simple for development and testing

* **Session-based authentication**
  Demonstrates maintaining user state across requests

* **Modular backend structure**
  Improves readability and scalability

---

## What I Learned

* Building a full-stack application from scratch
* Designing and consuming REST-style APIs
* Managing application state between frontend and backend
* Structuring backend code for clarity and maintainability

---

## Future Improvements

* Task editing and completion toggles
* Improved password security (salted hashing)
* Better validation and error handling
* Task filtering and sorting
* Deployment (e.g., Render, Railway)

---

## License

This project is available for educational and portfolio use.
