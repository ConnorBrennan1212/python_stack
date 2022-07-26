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

@app.route('/users/login', methods=['POST'])
def login_user():
    users = User.get_user_by_email({'email': request.form['email']})

    if len(users) != 1:
        flash('email or password incorrect')
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('username or password incorrect')
        return redirect('/')

    session['user_id'] = user.id
    session['email'] = user.email
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name


    print('log in ok')

    return redirect('/success')

@app.route('/success')
def success():
    if 'user_id' not in session:
        flash('log in to view')
        return redirect('/')
    return render_template('account.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("logged out")
    return redirect('/')
