from telethon.client import TelegramClient
from telethon.sessions import StringSession
import os
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
                

with TelegramClient(StringSession(os.environ.get("STRING_SESSION")), int(os.environ.get("API_ID")), os.environ.get("API_HASH")) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, MAZAFUCKA'))

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

