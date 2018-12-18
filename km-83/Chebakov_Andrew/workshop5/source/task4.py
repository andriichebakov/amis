import plotly
import plotly.graph_objs as go
from data import dataset

data = dict()

for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            if name in data:
                data[name] += float(dataset[name][date][product]['price'])
            else:
                data[name] = float(dataset[name][date][product]['price'])

print(data)

diagram = [go.Bar(x=list(data.keys()), y=list(data.values()))]
#plotly.offline.plot(diagram, filename='spending_graph.html')