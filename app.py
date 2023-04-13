from flask import Flask, request, make_response
from faunadb import query as q
from ussd_codes import abort_convo, start_convo, continue_convo , close_convo
import requests


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    print("it works")

@app.route("/ussdSessionEvent/new", methods=["POST"])
def start():
    print("stage 1")
    start_convo.replies(request)    

@app.route("/ussdSessionEvent/continue", methods=["POST"])
def continue_reply():
    continue_convo.replies(request)

@app.route("/ussdSessionEvent/close", methods=["POST"])
def close():
    close_convo.replies(request)

@app.route("/ussdSessionEvent/abort", methods=["POST"])
def abort():
    abort_convo.replies(request)

if __name__ == '__main__': 
    app.run(debug=True)
