from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return {"Result": "Hey Hi DhanuSree, How are you?."}
