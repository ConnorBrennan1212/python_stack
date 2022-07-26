from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register_user():
    #validate the data
    if User.validate_user(request.form):
        print("registration ok")
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':bcrypt.generate_password_hash(request.form['password']),
        }
        User.register_user(data)
        flash('user registered, log in now')
    else:
        print('validation fails')
    #create the user in database
    return redirect('/')