from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome_msg():
    """ returns 'welcome' """

    return "welcome"

@app.get("/welcome/home")
def welcome_home_msg():
    """ returns 'welcome home' """

    return "welcome home"

@app.get("/welcome/back")
def welcome_back_msg():
    """ returns 'welcome back' """

    return "welcome back"
