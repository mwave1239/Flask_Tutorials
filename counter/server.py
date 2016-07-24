from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)

app.secret_key = 'Secret'
counter = 1

def keepCount():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')

def start():
    keepCount()
    return render_template('index.html')

app.run(debug=True)
