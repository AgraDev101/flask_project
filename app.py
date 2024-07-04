from flask import Flask
# from db import connection
from weather_api import weather_api
from tasks import tasks_api
from short_url_api import short_url_api

app = Flask(__name__)

app.register_blueprint(weather_api)
app.register_blueprint(tasks_api)
app.register_blueprint(short_url_api)

# use "python app.py" to run

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/")
# def home():
#     x = 12
#     return render_template("index.html", data=x)

# @app.route("/tasks", methods= ['GET', "POST"])
# def read():
#     if request.method == "GET":
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM tasks")
#             result = cursor.fetchall()
#             print(result)
#             return jsonify({ "data": result }), 200
#     if request.method == "POST":
#         try:
#             with connection.cursor() as cursor:
#                 data = request.get_json()
#                 task = data['title']
#                 age = data['age']
#                 print(task, age)
#                 cursor.execute("INSERT INTO tasks (title, age) VALUES (%s, %s)", (task, age))
#                 connection.commit()
#                 return jsonify({ "task": task, "age": age }), 201
#         except Exception as e:
#             return jsonify({"message": "error" }), 500
    
# @app.route("/update", methods=['PUT'])
# def update():
#     with connection.cursor() as cursor:
#         data = request.get_json()
#         id = data['id']
#         task = data['title']
#         cursor.execute("UPDATE tasks SET title = %s WHERE id = %s", (task, id))
#         connection.commit()
#         return {"task": task}
    
# @app.route("/delete", methods=['DELETE'])
# def delete():
#     try:
#         with connection.cursor() as cursor:
#             data = request.get_json()
#             id = data['id']
#             print(id)
#             cursor.execute("DELETE from tasks WHERE id = %s", ())
#             connection.commit()
#             return "deleted"
#     except Exception as e:
#         return {"message": "query didn't run"}
