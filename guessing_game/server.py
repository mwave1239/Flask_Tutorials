from flask import Flask, session, render_template, request, session, redirect

import random

app = Flask(__name__)

app.secret_key = 'Secret'
#session['random_num'] = random.randrange(0,101)

@app.route('/')

def start():
    if not session.get('number'):
        session['number'] = random.randrange(1,101)
    return render_template('index.html')

@app.route('/check', methods=["POST"])

def check():
    session['low'] = False
    session['high'] = False
    session['correct'] = False
    if session['number'] == int(request.form['user_guess']):
        session['correct'] = True
    elif session['number'] > int(request.form['user_guess']):
        session['low'] = True
    elif session['number'] < int(request.form['user_guess']):
        session['high'] = True
    return redirect('/')

@app.route('/reset', methods=['GET'])

def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
