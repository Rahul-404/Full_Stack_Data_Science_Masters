from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
