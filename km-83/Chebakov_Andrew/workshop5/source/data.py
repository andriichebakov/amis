file = open('data/orders.csv')

info = file.read()

lines = info.splitlines()

clients = []
for client in lines[1:]:
    clients.append(client.split(', '))

dataset = dict()

for client in clients:
    name = client[0]
    date = client[1]
    product = client[2]
    quantity = client[3]
    price = client[4]
    if name in dataset:
        if date in dataset[name]:
            if product in dataset[name][date]:
                dataset[name][date][product]['quantity'] += quantity
                dataset[name][date][product]['price'] += price
            else:
                dataset[name][date][product] = {'quantity': quantity,
                                                'price': price}
        else:
            dataset[name][date] = {product: {'quantity': quantity,
                                             'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity,
                                          'price': price}}}
print(dataset)

file.close()