from flask import request, session
from datetime import datetime
import sqlite3

from models import *

def register_routes(app):

    @app.route('/signup')
    def signup():
        username = request.args.get('username')
        password = request.args.get('password')

        if not username or not password:
            return {"error": "Missing username or password"}

        try:
            create_user(username, password)
            return {"status": "user created"}
        except sqlite3.IntegrityError:
            return {"error": "username exists"}

    @app.route('/login')
    def login():
        username = request.args.get('username')
        password = request.args.get('password')

        user = find_user(username, password)

        if user:
            session['user_id'] = user[0]
            return {"status": "logged in"}
        return {"error": "invalid credentials"}

    @app.route('/tasks')
    def tasks():
        if 'user_id' not in session:
            return {"error": "not logged in"}

        rows = get_tasks(session['user_id'])
        return {"tasks": rows}

    @app.route('/add-task')
    def add_task_route():
        if 'user_id' not in session:
            return {"error": "not logged in"}

        title = request.args.get('title')
        date = request.args.get('date')

        if not title:
            return {"error": "missing title"}

        create_task(title, date, session['user_id'])
        return {"status": "task added"}

    @app.route('/remove-task')
    def remove_task():
        if 'user_id' not in session:
            return {"error": "not logged in"}

        task_id = request.args.get('id')

        if not task_id:
            return {"error": "missing id"}

        delete_task(task_id, session['user_id'])
        return {"status": "task deleted"}