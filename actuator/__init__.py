# __init__.py
from flask import Flask, render_template, redirect


def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route('/')
    def app_html():
        return render_template("app_html.html")

    @app.route('/actuator')
    def actuator():
        return redirect ("http://127.0.0.1:8000/pyctuator/health")




    return app

