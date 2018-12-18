from data import dataset, clients

all_products = {position[2] for position in clients}

for product in all_products:
    counter = 0
    for name in dataset:
        for date in dataset[name]:
            if product in dataset[name][date]:
                counter += 1
                break
    if counter == len(dataset.keys()):
        print('Everyone bought', product)
