from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "HEPSI": "Hellooo myself HEPSIBAAAAA",
        "DHANU": "Hello, Hepsi how are you?",
        "HEPSI2": "I'm fine, thankyou HRU"
    }
