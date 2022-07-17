from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", x = 8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def checkerboardwidth(x):
    return render_template("index.html", x=x, y=8, color1='red', color2 = 'black')

@app.route('/<int:x>/<int:y>')
def checkerboard_w_and_h(x,y):

    return render_template("index.html", x=x, y=y, color1='red', color2 = 'black')



if __name__ == '__main__':
    app.run(debug=True)