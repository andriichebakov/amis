from data import dataset


def new_position(dataset, name, date, product, price, quantity):
    if name in dataset:
        if date in dataset[name]:
            dataset[name][date][product] = {'quantity': quantity,
                                            'price': price}
        else:
            dataset[name][date] = {product: {'quantity': quantity,
                                             'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity,
                                          'price': price}}}


new_position(dataset, 'Bob', '01.01.2019', 'apple', 100, 50)
new_position(dataset, 'Jane', '10.11.2018', 'spice', 2000, 2)
new_position(dataset, 'Jane', '05.11.2018', 'spice', 2000, 2)

print(dataset)