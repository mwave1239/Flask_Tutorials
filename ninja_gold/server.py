from flask import Flask, render_template, redirect, request, session, url_for
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "SecretKeyDont"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	try:
		session['gold']
	except KeyError:
		session['gold'] = 0

	try:
		session['activities']
	except KeyError:
		session['activities'] = []

	if request.form['building'] == 'farm':
		gold = random.randrange(10,21)
	elif request.form['building'] == 'cave':
		gold = random.randrange(5,11)
	elif request.form['building'] == 'house':
		gold = random.randrange(2,6)
	elif request.form['building'] == 'casino':
		gold = random.randrange(-50,51)

	activity = ''
	time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
	if gold >= 0:
		activity += 'Earned ' + str(gold) + ' gold from the ' + str(request.form['building'] + '.')
	else:
		activity += 'Entered a casino and lost ' + str(gold) + ' gold. Yikes.'

	activity += ' (' + str(time) + ')'
	session['gold'] += gold
	session['activities'].insert(0, activity)
	return redirect(url_for('index'))

@app.route('/reset')
def reset():
	session.pop('gold')
	session.pop('activities')
	return redirect(url_for('index'))

app.run(debug=True)
