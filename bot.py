import os
import time
import requests
from flask import Flask

TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

def send_message(text):
    if not TOKEN or not CHAT_ID:
        print("TELEGRAM_TOKEN or TELEGRAM_CHAT_ID not set")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Failed to send message:", e)

app = Flask(__name__)

@app.route("/")
def index():
    send_message("Нагадування: cплатити податки 💸")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)