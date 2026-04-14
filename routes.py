from flask import request, session, jsonify, render_template
import sqlite3

from models import *

def register_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['POST']) # changed to post because sending data
    def signup():
        # Using request .json allows user to send data properly from frontend
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}),400

        try:
            create_user(username, password)
            # 201 = created (Standard for successfully adding somethig to a DB)
            return jsonify({"message": "User created successfully"}), 201
        except sqlite3.IntegrityError:
            # 409 = Conflict (The username already taken)
            return jsonify({"error": "Username already exists"}), 409

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = find_user(data.get('username'), data.get('password'))

        if user:
            session['user_id'] = user[0]
            return {"status": "logged in"}
        
        # 401 = Unauthorized (Wrong password/username)
        return jsonify ({"error": "Invalid credentials"}), 401

    @app.route('/tasks')
    def tasks():
        if 'user_id' not in session:
            return jsonify({"error": "Login required"}), 401

        rows = get_tasks(session['user_id'])
        
        # Cleaner json
        task_list = []
        for r in rows:
            task_list.append({
                "id": r[0],
                "title": r[1],
                "due_date": r[2],
                "completed": bool(r[3]) # Converts 0/1 from SQLite to True/False
            })

        return jsonify({"tasks": task_list}), 200

    @app.route('/add-task', methods=['POST'])
    def add_task_route():
        # Check if users are logged in
        if 'user_id' not in session:
            return jsonify({"error": "Not logged in"}), 401

        # Get data from JSON body instead of the URL
        data = request.get_json()
        title = data.get('title')
        date = data.get('date')

        # Validation: dont let them save an empty task
        if not title:
            return jsonify({"error": "Missing title"}), 400

        create_task(title, date, session['user_id'])
        return jsonify({"status": "Task added"}),201

    @app.route('/remove-task', methods=['DELETE'])
    def remove_task():
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()
        task_id = data.get('id')

        if not task_id:
            return jsonify({"error": "Missing task ID"}),400

        delete_task(task_id, session['user_id'])
        return jsonify({"status": "task deleted"}),200