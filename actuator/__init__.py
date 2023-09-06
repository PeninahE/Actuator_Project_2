# __init__.py
from flask import Flask, render_template, redirect


def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route('/')
    def app_html():
        return render_template("app_html.html")

    @app.route('/actuator/{endpoint}')
    def actuator_results(endpoint):
        if endpoint == "health":
            return redirect("http://127.0.0.1:8000/pyctuator/health")

        elif endpoint == ",=metrics":
            return redirect("http://127.0.0.1:8000/pyctuator/metrics")

        elif endpoint == "env":
            return redirect("http://127.0.0.1:8000/pyctuator/env")

        elif endpoint == "logfile":
            return redirect("http://127.0.0.1:8000/pyctuator/logfile")

        elif endpoint == "httptrace":
            return redirect("http://127.0.0.1:8000/pyctuator/httptrace")

        elif endpoint == "threaddump":
            return redirect("http://127.0.0.1:8000/pyctuator/threaddump")
        else:
            print("endpoint not found")
    return app

