# __init__.py
#from requests import requests
import requests
from flask import Flask, render_template, redirect, request


def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route('/hello')
    def hello ():
        return "hello world"

    @app.route('/')
    def app_html():
        return render_template("app_html.html")

    @app.route('/actuator', methods = ['POST'])
    def actuator():
        status_choice = request.form['status']
        url = "http://127.0.0.1:8000/pyctuator/" + status_choice
        actuator_response = requests.get(url)

        if status_choice == "health":
            return render_template("health.html", result = actuator_response.text)

        # elif status_choice == ",=metrics":
        #     return redirect("http://127.0.0.1:8000/pyctuator/metrics")
        #
        # elif status_choice == "env":
        #     return redirect("http://127.0.0.1:8000/pyctuator/env")
        #
        # elif status_choice == "logfile":
        #     return redirect("http://127.0.0.1:8000/pyctuator/logfile")
        #
        # elif status_choice == "httptrace":
        #     return redirect("http://127.0.0.1:8000/pyctuator/httptrace")
        #
        # elif status_choice == "threaddump":
        #     return redirect("http://127.0.0.1:8000/pyctuator/threaddump")
        # else:
        #     print("status_choice not found")
    return app

