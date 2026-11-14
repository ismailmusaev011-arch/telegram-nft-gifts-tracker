
import os
import json
import urllib.request
import urllib.parse

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(message):
    if not BOT_TOKEN:
        raise ValueError("Не найден BOT_TOKEN")

    if not CHAT_ID:
        raise ValueError("Не найден CHAT_ID")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": message
    }).encode()

    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read())

    if not result.get("ok"):
        raise RuntimeError("Telegram не принял сообщение")

    print("Сообщение успешно отправлено!")


send_message("✅ Бот подключен! Уведомления работают.")
