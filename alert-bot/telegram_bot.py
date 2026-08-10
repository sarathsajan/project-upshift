import requests
import time
import read_creds

TELEGRAM_BOT_TOKEN = read_creds.TELEGRAM_BOT_TOKEN
CHAT_ID = read_creds.TELEGRAM_CHAT_ID
TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_telegram_message(message):
    print(message)
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url=TELEGRAM_SEND_MESSAGE_URL, data=payload)