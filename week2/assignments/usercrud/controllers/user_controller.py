from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('show.html')

