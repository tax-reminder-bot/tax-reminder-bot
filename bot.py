
import os
import telegram
from flask import Flask, request

app = Flask(__name__)
import sys

token = os.environ.get("TELEGRAM_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

if not token or not chat_id:
    print("❌ Секрети TELEGRAM_TOKEN або TELEGRAM_CHAT_ID не встановлені!")
    sys.exit(1)  # завершити без краху контейнера

bot = telegram.Bot(token=token)


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = os.environ["TELEGRAM_CHAT_ID"]
        bot.send_message(chat_id=chat_id, text="Нагадування про податки 🧾")
    return "ok"
