import os
from flask import *

application = app = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route("/login")
def login():
    return render_template('login.html')

@application.route("/signUp")
def signUp():
    return render_template('signup.html')

@application.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    application.debug = True
    application.run()
