class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.next
            return data

    def is_empty(self):
        return self.top is None

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2, episodes):
        if vertex1 not in self.graph:
            self.graph[vertex1] = {}
        if vertex2 not in self.graph:
            self.graph[vertex2] = {}
        self.graph[vertex1][vertex2] = episodes
        self.graph[vertex2][vertex1] = episodes

# Crear el grafo
star_wars_graph = Graph()

# Agregar personajes y sus conexiones con la cantidad de episodios
connections = [
    ("Luke Skywalker", "Darth Vader", 3),
    ("Luke Skywalker", "Leia", 6),
    ("Darth Vader", "Leia", 2),
    ("Darth Vader", "Boba Fett", 1),
    ("Yoda", "Boba Fett", 4),
    ("Leia", "Rey", 2),
    ("Rey", "Kylo Ren", 3),
    ("Chewbacca", "Han Solo", 7),
    ("Chewbacca", "R2-D2", 5),
    ("Han Solo", "R2-D2", 3),
    ("R2-D2", "BB-8", 4)
]

for p1, p2, episodes in connections:
    star_wars_graph.add_edge(p1, p2, episodes)

# Tarea a: Hallar el árbol de expansión mínimo y verificar si contiene a Yoda
def find_mst(graph):
    mst = Graph()
    visited = set()
    edge_list = []

    start_vertex = list(graph.graph.keys())[0]
    visited.add(start_vertex)

    for vertex, edges in graph.graph.items():
        for neighbor, episodes in edges.items():
            edge_list.append((vertex, neighbor, episodes))

    edge_list.sort(key=lambda edge: edge[2])

    while len(visited) < len(graph.graph):
        min_edge = None
        for edge in edge_list:
            _, neighbor, _ = edge
            if neighbor in visited:
                continue
            min_edge = edge
            break

        if min_edge:
            vertex, neighbor, episodes = min_edge
            visited.add(neighbor)
            mst.add_edge(vertex, neighbor, episodes)

    return mst

mst = find_mst(star_wars_graph)

print("Árbol de Expansión Mínimo:")
for vertex, edges in mst.graph.items():
    for neighbor, episodes in edges.items():
        print(f"{vertex} - {neighbor} ({episodes} episodios)")

contains_yoda = "Yoda" in mst.graph
print("¿El árbol contiene a Yoda?", contains_yoda)

# Tarea b: Número máximo de episodio compartido y personajes
max_episodes = 0
characters = []

for vertex, edges in star_wars_graph.graph.items():
    for neighbor, episodes in edges.items():
        if episodes > max_episodes:
            max_episodes = episodes
            characters = [(vertex, neighbor)]
        elif episodes == max_episodes:
            characters.append((vertex, neighbor))

print("\nMáximo número de episodios compartidos:", max_episodes)
print("Personajes que comparten este máximo:")
for character1, character2 in characters:
    print(f"{character1} - {character2}")
