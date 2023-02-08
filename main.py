
import requests
import os
from flask import Flask, request, Response
app = Flask(__name__)

data = {"a": "as"}

@app.route('/', methods=['HEAD'])
def handle_request():
    requests.post(os.environ.get('LINK'), data=data)
    return ""
    

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))


