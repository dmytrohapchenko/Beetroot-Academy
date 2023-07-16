def main():
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    full_price = 0
    for i in stock:
        for j in prices:
            if i == j:
                full_price += stock.get(i) * prices.get(j)
            continue
    return full_price


if __name__ == '__main__':
    print(main())
