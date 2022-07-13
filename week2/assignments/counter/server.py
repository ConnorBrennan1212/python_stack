from glob import glob
from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

realcount = 0
count = 0

@app.route('/')
def counter():
    global count
    global realcount
    count += 1
    realcount +=1
    print(realcount)
    return render_template('index.html',count = count, realcount = realcount)

@app.route('/addtwo',methods = ['POST'])
def addtwo():
    global count
    count +=1
    return redirect('/')

@app.route('/reset')
def reset():
    global count
    count=0
    return render_template('index.html',count = count)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
