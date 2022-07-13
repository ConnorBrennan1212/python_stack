from distutils.log import info
from flask import Flask, render_template, redirect, session
app=Flask(__name__)

info ={
}

locations = ["Chicago", "Seattle", "Online", "Burbank"]
language = [{"Python"}, {"C#"}, {"javascript"}, {"css"}, {"html"}]


@app.route('/')
def survey():
    return render_template('index.html', language = language, locations = locations)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)