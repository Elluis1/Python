import networkx as nx

# Crear el grafo no dirigido
G = nx.Graph()

# Definir los ambientes de la casa como vértices
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño1", "baño2", "habitacion1", "habitacion2", "sala_de_estar", "terraza", "patio"]

# Agregar vértices al grafo
G.add_nodes_from(ambientes)

# Agregar aristas al grafo con pesos (distancia en metros)
aristas = [
    ("cocina", "comedor", 5), ("cocina", "cochera", 8), ("cocina", "habitacion1", 3),
    ("comedor", "cochera", 6), ("comedor", "habitacion2", 5), ("cochera", "quincho", 7),
    ("quincho", "baño1", 4), ("quincho", "baño2", 6), ("quincho", "terraza", 8),
    ("baño1", "habitacion1", 2), ("baño2", "habitacion2", 4),
    ("habitacion1", "sala_de_estar", 7), ("sala_de_estar", "habitacion2", 6),
    ("sala_de_estar", "patio", 9), ("terraza", "patio", 5)
]

G.add_weighted_edges_from(aristas)

# c. Obtener el árbol de expansión mínima y determinar la longitud total de cables
arbol_expansion_minima = nx.minimum_spanning_tree(G)
longitud_total_cables = sum(weight for _, _, weight in arbol_expansion_minima.edges(data="weight"))
print("Árbol de expansión mínima:")
print(list(arbol_expansion_minima.edges()))
print(f"Longitud total de cables necesarios: {longitud_total_cables} metros")

# d. Determinar el camino más corto desde habitacion1 hasta sala_de_estar
camino_mas_corto = nx.shortest_path(G, source="habitacion1", target="sala_de_estar", weight="weight")
longitud_camino_mas_corto = nx.shortest_path_length(G, source="habitacion1", target="sala_de_estar", weight="weight")
print("Camino más corto desde habitacion 1 hasta sala_de_estar:")
print(camino_mas_corto)
print(f"Longitud del camino más corto: {longitud_camino_mas_corto} metros")
