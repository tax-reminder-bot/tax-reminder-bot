import os
import telebot
import datetime

# Токен твого Telegram-бота
TOKEN = '7660525712:AAF7gNF_ybwQ8wh6dY-K8vxjtr0RbnQT57c'

# Ініціалізація бота
bot = telebot.TeleBot(TOKEN)

# ID твого чату (буде отриманий після першого запуску)
CHAT_ID = os.getenv("CHAT_ID")

# Функція для створення повідомлення
def generate_message():
    month_name = datetime.datetime.now().strftime("%B")
    message = f"""🔔 Нагадування про податки на {month_name} 2025 року:

За ФОП 2 групи:
• Єдиний податок: 1 820 грн
• ЄСВ: 2 002 грн
• Військовий збір: (сплачується авансом за квартал)

За 1 працівника:
• ПДФО: 1 638 грн
• ВЗ: 137 грн
• ЄСВ: 2 002 грн

Разом за працівника: 11 102 грн

🕐 Термін сплати: до 20 числа поточного місяця!
"""
    return message

# Відправлення повідомлення
def send_reminder():
    if CHAT_ID:
        bot.send_message(CHAT_ID, generate_message())
    else:
        print("CHAT_ID не встановлений.")

if __name__ == "__main__":
    send_reminder()