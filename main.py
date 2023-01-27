import telethon
import os
import time

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
client = telethon.TelegramClient(os.environ.get("SNAME"), api_id, api_hash)
client.start()
client.run_until_disconnected()
