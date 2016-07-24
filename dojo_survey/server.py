from flask import Flask, render_template, redirect, request, session, flash, url_for

app = Flask(__name__)
app.secret_key = "SecretKeyDont"

@app.route('/')

def start():
    return render_template('index.html')

@app.route('/result', methods=["POST"])

def result():
    if len(request.form['your_name']) < 1:
        flash("Name cannot be blank")
        return redirect('/')
    elif request.form['comment'] == '':
        flash("Comments cannot be blank")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comments cannot be more than 120 characters")
        return redirect('/')
    return render_template('submit.html', name = request.form['your_name'], location = request.form['dojo_location'], language = request.form['fav_language'], comment = request.form['comment'] )

app.run(debug=True)
