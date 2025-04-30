
import os
import time
import requests
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

MIN_SALARY_UAH = 8000
PENSION_PERCENT = 22
INCOME_TAX_PERCENT = 18
WAR_TAX_PERCENT = 1.5

def calculate_taxes(salary):
    pension = salary * PENSION_PERCENT / 100
    income_tax = salary * INCOME_TAX_PERCENT / 100
    war_tax = salary * WAR_TAX_PERCENT / 100
    return pension, income_tax, war_tax

def send_notification():
    today = datetime.now()
    if today.day == 17:
        pension, income_tax, war_tax = calculate_taxes(MIN_SALARY_UAH)
        total = pension + income_tax + war_tax
        text = f"Нагадування: сьогодні 17 число!\n\nЄСВ: {pension:.2f} грн\nПДФО: {income_tax:.2f} грн\nВійськовий збір: {war_tax:.2f} грн\nВсього: {total:.2f} грн"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})

if __name__ == "__main__":
    while True:
        send_notification()
        time.sleep(86400)
