from flask import Flask, render_template
from utils import load_model

app = Flask(__name__)

# load model
model = load_model("./models/my_model.h5")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
