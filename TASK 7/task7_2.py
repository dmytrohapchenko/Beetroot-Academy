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
count = 0
for i in range(len(stock)):
    count += stock[list(stock.keys())[i]] * prices[list(prices.keys())[i]]
print(count)

