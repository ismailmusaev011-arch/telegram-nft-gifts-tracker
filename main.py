
MAX_PRICE = 2000

gifts = [
    {
        "name": "Teddy Bear",
        "seller": "@seller1",
        "price": 1200
    },
    {
        "name": "Plush Pepe",
        "seller": "@seller2",
        "price": 2500
    },
    {
        "name": "Durov's Cap",
        "seller": "@seller3",
        "price": 1800
    },
    {
        "name": "Signet Ring",
        "seller": "@seller4",
        "price": 900
    }
]


def find_gifts(gifts):
    suitable = []

    for gift in gifts:
        if 0 < gift["price"] <= MAX_PRICE:
            suitable.append(gift)

    return suitable


if __name__ == "__main__":
    results = find_gifts(gifts)

    print("🎁 NFT GIFTS TRACKER")
    print("Максимальная цена: 2000 ⭐")
    print("--------------------")

    for gift in results:
        print(f"🎁 {gift['name']}")
        print(f"👤 Продавец: {gift['seller']}")
        print(f"⭐ Цена: {gift['price']}")
        print("--------------------")

    print(f"Найдено подарков: {len(results)}")
