from flask import Flask, render_template, request, send_file, jsonify
import google.generativeai as palm
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Configure the API key
palm.configure(api_key="AIzaSyDQegtx6ycbXTp7treDwhdzmba2V6WdSQ0")

# Define the model
model = "models/chat-bison-001"

app = Flask(__name__)

def generate_business_idea():
    response = palm.chat(model=model, messages=["Generate 10 business ideas, please do not include any description."])
    return response.last

def generate_catchphrase():
    response = palm.chat(model=model, messages=["Generate 10 catchphrases for a business, without any description."])
    return response.last

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catchphrases")
def catchphrases():
    catchphrase = generate_catchphrase()
    return render_template("catchphrases.html", catchphrase=catchphrase)

@app.route("/logos")
def logos():
    return render_template("logos.html")

@app.route("/business_ideas")
def business_ideas():
    business_idea = generate_business_idea()
    return render_template("business_ideas.html", business_idea=business_idea)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
