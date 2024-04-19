import asyncio
import os

import dotenv
from flask import Flask
from telethon import TelegramClient

dotenv.load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
chat_id = os.getenv('CHAT_ID')

app = Flask(__name__)


async def send_message():
    print('Start ASYNC')
    try:
        async with TelegramClient('cont1', int(api_id), api_hash) as client:
            await client.send_message(chat_id, '/pidor@SublimeBot')
        print("SEND MESSAGE")
    except Exception as ex:
        print(f"ERROR -> {ex}")


@app.route('/')
def method_get():
    print("GET")
    asyncio.run(send_message())
    return 'Send Message -> GET'


@app.route('/', methods=['POST'])
def submit():
    print("POST")
    asyncio.run(send_message())
    return 'Send Message -> POST'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
