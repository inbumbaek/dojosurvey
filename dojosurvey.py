from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    return render_template("dojosurvey.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/clear')
def clear():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)