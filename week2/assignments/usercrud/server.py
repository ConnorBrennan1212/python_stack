from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('users')
def index():
    return render_template('show.html', users=User.get_all())

if __name__=="__main__":
    app.run(debug=True)