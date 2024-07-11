from flask import Blueprint, jsonify
import requests

weather_api = Blueprint("weather_api", __name__)

url = "https://www.weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=ZWL008554"

@weather_api.route("/weather")
def get_weather():
    # url = "https://www.weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=ZWL008554"
    res = requests.get(url, headers={ "x-zomato-api-key" :"enter api key here"})
    print(res.json())
    return jsonify({"data": res.json()})
