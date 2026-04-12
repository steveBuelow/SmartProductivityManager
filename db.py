import sqlite3

def get_db():
    conn = sqlite3.connect('test.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    with get_db() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            );

            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                completed BOOLEAN DEFAULT 0,
                due_date TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        ''')