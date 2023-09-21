from glob import escape
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('Pori roky.html')

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/bye/<name>")
def bye(name):
    return f"Bye, {escape(name)}!"



'''@app.route("/main")
def main():
    return "<p>The Main(base)</p>
    "<p>Hello, World! I`m Max(OrIgInSzz)</p>""'''

app.run()