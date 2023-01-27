import telethon
import os
import time
import flask
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.headers.get('content-type') == "application/json":
        return ""
    else:
        flask.abort(403)
    if request.method == "POST":
        return Response("OK", status=200)
    else:
        return ""
                
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
client = telethon.TelegramClient(os.environ.get("SNAME"), api_id, api_hash)
client.start()
client.run_until_disconnected()

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

