import openai
import os
import flask
from flask import Flask, request, Response
import telebot
app = Flask(__name__)
bot = telebot.TeleBot(os.environ.get("TOKEN"))
openai.api_key = os.environ.get("OPENAI_KEY")

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.headers.get('content-type') == "application/json":
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)
    if request.method == "POST":
        return Response("OK", status=200)
    else:
        return ""

@bot.message_handler(commands=["cgpt"])
def getOAIResponse(message):
    if message.text != "/cgpt":
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            max_tokens=2048,
            temperature=0.5,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
    else:
        bot.send_message(chat_id=message.from_user.id, text="Please, enter the valid message like this:\n"
                                                            f"{message.text} describe fantasy world")

@bot.message_handler(commands=["image"])
def openAIImage(message):
    # print(message.text)
    if message.text != "/image":
        try:
            response = openai.Image.create(
                prompt=message.text,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            # print(image_url)
            bot.send_photo(chat_id=message.from_user.id, photo=image_url)
        except openai.error.InvalidRequestError as e:
            bot.send_message(chat_id=message.from_user.id, text=str(e))
    else:
        bot.send_message(chat_id=message.from_user.id, text="Please, enter the valid message like this:\n"
                                                            f"{message.text} describe fantasy world")


app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
