from flask import Flask, redirect, url_for, render_template
from werkzeug.utils import html

app = Flask(__name__)

# Define home page.
@app.route("/") # This is the route to this page.
def home():
    return render_template("index.html", content="Testing")
html

if __name__ == "__main__":
    app.run(debug=True)