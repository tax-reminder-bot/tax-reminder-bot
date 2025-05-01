import os
import sys
import telegram
from flask import Flask

app = Flask(__name__)

token = os.environ.get("TELEGRAM_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

if not token or not chat_id:
    print("❌ Помилка: TELEGRAM_TOKEN або TELEGRAM_CHAT_ID не передані як секрети Fly.io!")
    sys.exit(1)

bot = telegram.Bot(token=token)

@app.route("/")
def index():
    bot.send_message(chat_id=chat_id, text="✅ Нагадування про податки!")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
