from flask import Flask, render_template, request
from functions import functions

app = Flask(__name__)
funcs = functions()


@app.route('/')
def hello_poll():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


##########################################
@app.route('/create_poll', methods=['POST'])
def create_poll():
    return funcs.printForm(request.form)


if __name__ == '__main__':
    app.run(debug=True)
