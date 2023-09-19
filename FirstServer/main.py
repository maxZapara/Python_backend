from glob import escape
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! I`m Max(OrIgInSzz)</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/bye/<name>")
def bye(name):
    return f"Bye, {escape(name)}!"

app.run()