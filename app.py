from flask import Flask, render_template, request, redirect, url_for, session
from PIL import Image
from matplotlib import image
from utils import load_model, predict

app = Flask(__name__)

# load model
model = load_model("./models/my_model.h5")

# pred = predict("./test.png", model)
# image.imsave("pred.png", pred, cmap="gray")


@app.route("/")
def index():
    return render_template("index.html", image=False)


@app.route("/", methods=["POST"])
def predict_image():
    image_upload = request.files["image"]
    if image_upload != "":
        img = Image.open(image_upload)
        img = img.resize((512, 512))
        img.save("./static/test.png")
    return render_template("index.html", image=True, image_url="/static/test.png")
