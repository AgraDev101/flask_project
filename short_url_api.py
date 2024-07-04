from flask import Blueprint, request, jsonify, redirect
from db import connection
from nanoid import generate

short_url_api = Blueprint("short_url_api", __name__)

@short_url_api.route("/url", methods= ['GET', "POST"])
def get_url():
    try:
        with connection.cursor() as cursor:
            data = request.get_json()
            url = data['url']
            print(url)
            id = generate('1234567890abcdef', 10)
            cursor.execute("INSERT INTO urls (original_url, short_url) VALUES (%s, %s)", (url, id))
            connection.commit()
            cursor.close()
            short_url = request.host_url + "url/" + id
            return jsonify({ "data": short_url }), 201
    except Exception as e:
        return jsonify({"data": "error"})
    
@short_url_api.route("/url/<id>", methods= ['GET'])
def redirect_url(id):
    try:
        with connection.cursor() as cursor:
            print(id)
            cursor.execute("SELECT original_url FROM urls WHERE short_url = %s", (id))
            result = cursor.fetchall()
            cursor.close()
            print(result)
            return redirect(result[0]['original_url'])
    except Exception as e:
        return jsonify({"data": "error"})