from db import get_db
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )

def find_user(username, password):
    with get_db() as conn:
        return conn.execute(
            "SELECT id FROM users WHERE username=? AND password=?",
            (username, hash_password(password))
        ).fetchone()

def create_task(title, date, user_id):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO tasks (title, due_date, user_id) VALUES (?, ?, ?)",
            (title, date, user_id)
        )

def get_tasks(user_id):
    with get_db() as conn:
        return conn.execute(
            "SELECT id, title, due_date, completed FROM tasks WHERE user_id=?",
            (user_id,)
        ).fetchall()

def delete_task(task_id, user_id):
    with get_db() as conn:
        conn.execute(
            "DELETE FROM tasks WHERE id=? AND user_id=?",
            (task_id, user_id)
        )