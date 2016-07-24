from flask import Flask, render_template, redirect, request, session, flash, url_for
import re

#check for email completeness
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "SecretKeyDont"

@app.route('/')

def start():
    return render_template('index.html')

@app.route('/result', methods=["POST"])

def result():
    errors = False
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    elif len(request.form['first_name']) < 1:
        flash("First name cannot be blank!")
        errors = True
    elif len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!")
        errors = True
    elif len(request.form['password']) < 1:
        flash("Password field cannot be blank!")
        errors = True
    elif len(request.form['password_confirm']) < 1:
        flash("Password confirmation cannot be blank!")
        errors = True
    elif first_name.isdigit() == True:
        flash("First name shouldn't have digits!")
        errors = True
    elif last_name.isdigit() == True:
        flash("Last name shouldn't have digits!")
        errors = True
    elif len(request.form['password']) < 8:
        flash("Password should be more than 8 characters")
        errors = True
    elif request.form['password'] != request.form['password_confirm']:
        flash("Your passwords do not match!")
        errors = True
    if errors == True:
        return redirect('/')
    else:
        return render_template('submit.html')

app.run(debug=True)
