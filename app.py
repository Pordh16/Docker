from flask import *

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>hello<h1>"

@app.route("/buy")
def buy():
    return "<h2>Buy me<h2>"

if __name__ == "__main__":
    app.run(debug=True)