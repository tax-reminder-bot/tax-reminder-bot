import os
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт! Це бот-нагадувач про податки.")

def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()