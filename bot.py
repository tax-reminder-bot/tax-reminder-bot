
import os
import telegram
from flask import Flask, request

app = Flask(__name__)
bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = os.environ["TELEGRAM_CHAT_ID"]
        bot.send_message(chat_id=chat_id, text="Нагадування про податки 🧾")
    return "ok"
