import os
import telegram
import sys

token = os.environ.get("TELEGRAM_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

if not token:
    print("❌ TELEGRAM_TOKEN is not set")
    sys.exit(1)

if not chat_id:
    print("❌ TELEGRAM_CHAT_ID is not set")
    sys.exit(1)

bot = telegram.Bot(token=token)

@app.route("/")
def index():
    bot.send_message(chat_id=chat_id, text="✅ Нагадування про податки!")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
