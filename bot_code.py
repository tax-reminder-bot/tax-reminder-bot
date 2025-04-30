import os
import requests
from bs4 import BeautifulSoup
import datetime
import telebot

# Токен Telegram-бота
TOKEN = '7660525712:AAF7gNF_ybwQ8wh6dY-K8vxjtr0RbnQT57c'
bot = telebot.TeleBot(TOKEN)
CHAT_ID = os.getenv("CHAT_ID")

# Функція для отримання актуальної мінімальної зарплати
def get_min_salary():
    url = 'https://index.minfin.com.ua/ua/labour/salary/min/'
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        return 9100  # fallback
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2 and '2025' in cells[0].text:
            return int(cells[1].text.replace(' ', '').strip())
    return 9100  # fallback

# Формування повідомлення
def generate_message(min_salary):
    esv = round(min_salary * 0.22)
    pdfo = round(min_salary * 0.18)
    vz = round(min_salary * 0.015)
    total_worker = esv + pdfo + vz
    message = f"""🔔 Нагадування про податки на {datetime.datetime.now().strftime('%B')} 2025 року:

📌 Мінімальна зарплата: {min_salary} грн

За ФОП 2 групи:
• Єдиний податок: 1 820 грн
• ЄСВ: {esv} грн

За 1 працівника:
• ПДФО: {pdfo} грн
• ВЗ: {vz} грн
• ЄСВ: {esv} грн

Разом за працівника: {total_worker} грн

🕐 Термін сплати: до 20 числа поточного місяця!"""
    return message

# Основна функція запуску
if __name__ == '__main__':
    today = datetime.datetime.now()
    if CHAT_ID:
        if today.day == 18:
            min_salary = get_min_salary()
            bot.send_message(CHAT_ID, generate_message(min_salary))
        else:
            print(f"Сьогодні {today.day}-те число. Повідомлення не надсилається.")
    else:
        print("CHAT_ID не встановлений.")