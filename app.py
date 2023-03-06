from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}'


if __name__ == '__main__':
    app.run()
