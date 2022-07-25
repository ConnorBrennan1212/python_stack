from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/new/ninja')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('newninja.html', dojos=all_dojos)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')




