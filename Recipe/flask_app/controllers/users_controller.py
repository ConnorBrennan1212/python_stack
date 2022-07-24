from flask_app import app
from flask import render_template, request, redirect

@app.route('/')
def display_login():
    return render_template('login.html')

@app.route('user/registration', methods = ['POST'])
def process_registration():
    #validate the registration form
    #connect to the model
    #validate if the user already exists
    #proceed to create the user
