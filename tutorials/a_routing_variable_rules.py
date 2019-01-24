from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
    return "hello world "

def helloworld_user():
    return "hello world user"

@app.route('/welcome/<name>')
def welcome(name):
    return "welcome " + name

@app.route('/welcome/<int:num>')
def welcomenum(num):
    return "welcome " + str(num)

@app.route('/welcome_trailing_slash/')
def welcome_trailing_slash():
    return "welcome "


app.add_url_rule('/helloworld_user', view_func=helloworld_user)

app.debug=True

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)
