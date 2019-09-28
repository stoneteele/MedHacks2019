import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', msg='home')

@app.route("/login")
def login():
    return render_template('login.html', msg='login')

@app.route("/signUp")
def signUp():
    return render_template('signUp.html', msg='sign up')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', msg='dashboard')

app.run(host='0.0.0.0', port=5000)
