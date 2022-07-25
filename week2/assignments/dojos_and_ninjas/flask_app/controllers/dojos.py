from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    return render_template('newdojo.html', dojos=all_dojos)

@app.route('/dojo/add', methods=['POST'])
def add_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/show/ninjas/<int:Dojos_id>')
def show_ninja_dojo(Dojos_id):
    data={'id':Dojos_id}
    dojo = Dojo.show_ninja_dojo(data)
    return render_template('showninjas.html', dojo = dojo)