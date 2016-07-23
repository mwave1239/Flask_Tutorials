from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def start():
    return render_template('index.html')

@app.route('/result', methods=["POST"])

def result():
    return render_template('submit.html', name = request.form['your_name'], location = request.form['dojo_location'], language = request.form['fav_language'], comment = request.form['comment'] )

app.run(debug=True)
