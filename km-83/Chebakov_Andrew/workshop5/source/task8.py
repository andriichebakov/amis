from data import dataset
import plotly
import plotly.graph_objs as go

clients = dict()

for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            if product in clients:
                clients[product].update({name})
            else:
                clients[product] = {name}
print(clients)

for product in clients:
    clients[product] = len(clients[product])

diagram = [go.Bar(x=list(clients.keys()),
                  y=list(clients.values()))]
plotly.offline.plot(diagram, filename='ammount_of_buyers.html')