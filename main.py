
import os
import json
import urllib.request
import urllib.parse
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MAX_PRICE = 2000
CHECK_INTERVAL = 300

seen_gifts = set()


def telegram_request(method, params=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"

    data = urllib.parse.urlencode(params or {}).encode()

    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def send_message(message):
    result = telegram_request("sendMessage", {
        "chat_id": CHAT_ID,
        "text": message
    })

    if not result.get("ok"):
        raise RuntimeError("Ошибка отправки сообщения")


def get_gifts():
    result = telegram_request("getAvailableGifts")

    if not result.get("ok"):
        raise RuntimeError("Не удалось получить подарки")

    return result["result"]["gifts"]


def check_gifts():
    gifts = get_gifts()

    for gift in gifts:
        gift_id = str(gift["id"])
        price = gift.get("star_count", 0)

        if price <= MAX_PRICE and gift_id not in seen_gifts:
            seen_gifts.add(gift_id)

            name = gift.get("sticker", {}).get(
                "emoji", "🎁"
            )

            message = (
                "🎁 Найден подарок!\n\n"
                f"Название: {name}\n"
                f"Цена: {price} ⭐\n"
                f"ID: {gift_id}"
            )

            send_message(message)


def main():
    send_message("✅ NFT Gifts Tracker запущен!")

    while True:
        try:
            check_gifts()
            print("Проверка завершена")

        except Exception as error:
            print(f"Ошибка: {error}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
