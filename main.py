from flask import Flask, render_template, request, redirect
from urllib.request import urlopen
import json
import math
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'super secret key'

# go to openweathermap.org to recieve your API key!
api_key = "paste your api weather key here"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/showWeather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form.get("city")
    else:
        city = "Ahmedabad"

    weather_url = urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    weather_data = json.loads(weather_url.read())

    final_temp = math.trunc(weather_data['main']['temp']-273)

    icon_code = weather_data['weather'][0]['icon']

    status = weather_data['weather'][0]['main']

    wind_speed = weather_data['wind']['speed']

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    # print("Current Time =", current_time)
    return render_template("weather.html", weather = final_temp, city = city, iconcode = icon_code, status = status, wind = wind_speed, time = current_time)

@app.route("/home_redirect")
def redirect_to_home():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)