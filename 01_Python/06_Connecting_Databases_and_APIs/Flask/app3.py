from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World! 1 </h1>"

@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World! 2 </h1>"

@app.route("/test_fun")
def test():
    a = 5+6
    return "<h1> this is my first fun in flask {} </h1>".format(a)

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "<h1> this is my input from url {} </h1>".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")