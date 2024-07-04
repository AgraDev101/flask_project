from flask import Blueprint, request, jsonify
from db import connection

tasks_api = Blueprint("tasks_api", __name__)

@tasks_api.route("/tasks", methods= ['GET', "POST"])
def read():
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks")
            result = cursor.fetchall()
            print(result)
            return jsonify({ "data": result }), 200
    if request.method == "POST":
        try:
            with connection.cursor() as cursor:
                data = request.get_json()
                task = data['title']
                age = data['age']
                print(task, age)
                cursor.execute("INSERT INTO tasks (title, age) VALUES (%s, %s)", (task, age))
                connection.commit()
                return jsonify({ "task": task, "age": age }), 201
        except Exception as e:
            return jsonify({"message": "error" }), 500