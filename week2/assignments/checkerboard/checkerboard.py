from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    x=8
    y=8
    color1 = 'red'
    color2 = 'blue'
    return render_template("index.html", x = x, y=y, color1=color1, color2=color2)

@app.route('/<x>')
def checkerboardwidth(x):
    x = int(x)
    color1='red'
    color2='blue'
    return render_template("index.html", x=x, color1=color1, color2 = color2)
    