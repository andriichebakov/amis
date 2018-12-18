from data import dataset

prices = dict()

for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            quantity = float(dataset[name][date][product]['quantity'])
            price = float(dataset[name][date][product]['price']) / quantity
            if product in prices:
                if prices[product] < price:
                    prices[product] = price
            prices[product] = price

print(prices)

biggest_price = max(list(prices.values()))
for product in prices:
    if prices[product] == biggest_price:
        print('The most expensive product is', product)
        break