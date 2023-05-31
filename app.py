import os
import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "s3cr3t"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")
db = 'save.txt'
cash = []
if db in os.listdir('.'):
    with open(db, 'rb') as x:
        cash = pickle.load(x)


@app.route("/", methods=["GET"])
def index():
    return render_template("layouts/index.html", data=cash)


@app.route("/save", methods=["POST"])
def save_name():
    name = request.form["name"]
    cash.append(name)
    return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    with open(db, 'wb') as x:
        pickle.dump(cash, x)
