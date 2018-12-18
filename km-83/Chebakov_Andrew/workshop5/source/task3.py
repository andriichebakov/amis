import plotly
import plotly.graph_objs as go
from data import dataset

dates = []
prices = []

for date in dataset['John']:
    if 'apple' in dataset['John'][date]:
        dates.append(date)
        quant, price = dataset['John'][date]['apple'].values()
        prices.append(float(price)/float(quant))

n = 1
while n < len(dates):
    for i in range(len(dates)-1):
        if dates[i] > dates[i+1]:
            dates[i], dates[i+1] = dates[i+1], dates[i]
            prices[i], prices[i+1] = prices[i+1], prices[i]
    n += 1

print(dates, prices)

diagram = [go.Scatter(x=dates, y=prices)]
plotly.offline.plot(diagram, filename='change_of_price.html')