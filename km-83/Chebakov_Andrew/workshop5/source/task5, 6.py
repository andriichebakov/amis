from data import dataset

volume = {}

for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            if product in volume:
                volume[product] += float(dataset[name][date][product]['quantity'])
            else:
                volume[product] = float(dataset[name][date][product]['quantity'])

print(volume)
max_volume = max(list(volume.values()))
min_volume = min(list(volume.values()))

for fruit in volume:
    if volume[fruit] == max_volume:
        print('Most popular product is', fruit)
    if volume[fruit] == min_volume:
        print('Least popular product is', fruit)