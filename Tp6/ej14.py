from classGraph import Graph

grafoCasa = Graph(False)

habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitacion 1', 'habitacion 2', 'sala de estar', 'terraza', 'patio']

class Habitacion():
    def __init__(self, name):
        self.name = name

for habitacion in habitaciones:
    grafoCasa.insert_vertice(habitacion)

grafoCasa.insert_arist('cocina', 'comedor', 20), grafoCasa.insert_arist('comedor', 'cochera', 14)
grafoCasa.insert_arist('cochera', 'quincho', 30), grafoCasa.insert_arist('quincho', 'baño 1', 3)
grafoCasa.insert_arist('baño 1', 'baño 2', 50), grafoCasa.insert_arist('baño 2', 'habitacion 1', 10)
grafoCasa.insert_arist('habitacion 1', 'habitacion 2', 17), grafoCasa.insert_arist('habitacion 2', 'sala de estar', 24)
grafoCasa.insert_arist('sala de estar', 'terraza', 14), grafoCasa.insert_arist('terraza', 'patio', 32)
grafoCasa.insert_arist('cocina', 'patio', 15), grafoCasa.insert_arist('comedor', 'terraza', 29)
grafoCasa.insert_arist('cochera', 'sala de estar', 4), grafoCasa.insert_arist('quincho', 'habitacion 2', 40)
grafoCasa.insert_arist('baño 1', 'habitacion 1', 7), grafoCasa.insert_arist('patio', 'comedor', 26)
grafoCasa.insert_arist('patio', 'sala de estar', 22), grafoCasa.insert_arist('patio', 'baño 1', 14)
grafoCasa.insert_arist('cocina', 'baño 2', 9), grafoCasa.insert_arist('comedor', 'sala de estar', 5)

print(grafoCasa.kruskal())
stack = grafoCasa.dijkstra('habitacion 1', 'sala de estar')

while stack.size() > 0:
    print(stack.on_top())
    stack.pop()