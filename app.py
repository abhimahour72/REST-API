from flask import Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Yoyofffo"



@app.route("/home")
def home():
    return "this is home"



from controller import *
