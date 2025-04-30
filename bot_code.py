import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise Exception("Missing TELEGRAM_TOKEN or TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Привіт! Це нагадування від твого бота :)")