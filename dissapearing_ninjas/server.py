from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "SecretKeyDont"

@app.route('/')

def start():
    return render_template('index.html')

@app.route('/ninja')

def ninja():
    display_turtles = True
    return render_template('ninjas.html', display_turtles=display_turtles)

@app.route('/ninja/<color>')

def color(color):
    display_turtles = False
    return render_template('ninjas.html', color = color, display_turtles = False)

app.run(debug = True)
