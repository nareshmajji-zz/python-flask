from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return request.form['nm']
    else:
        return request.args.get('nm')

app.debug=True

if __name__ == '__main__':
    app.run(debug=True)
