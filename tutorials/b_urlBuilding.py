from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome user"

@app.route('/welcome_guest')
def welcome_guest():
    return "welcome guest"

@app.route('/login/<name>')
def login(name):
    if name == 'admin':
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('welcome_guest'))


app.debug = True

if __name__ == "__main__":
    app.run(debug=True)