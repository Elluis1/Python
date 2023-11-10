import networkx as nx

# Definir el grafo para el primer ejercicio (maravillas arquitectónicas y naturales)
G = nx.Graph()

maravillas = [
    {"nombre": "Chichén Itzá", "pais": "México", "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": "Brasil", "tipo": "arquitectonica"},
    {"nombre": "Coliseo", "pais": "Italia", "tipo": "arquitectonica"},
    {"nombre": "Machu Picchu", "pais": "Perú", "tipo": "arquitectonica"},
    {"nombre": "Muralla China", "pais": "China", "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": "Jordania", "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": "India", "tipo": "arquitectonica"},
    {"nombre": "Amazonia", "pais": "Varios", "tipo": "natural"},
    {"nombre": "Bahía de Ha-Long", "pais": "Vietnam", "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": "Argentina", "tipo": "natural"},
    {"nombre": "Islas Galápagos", "pais": "Ecuador", "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": "Sudáfrica", "tipo": "natural"},
    {"nombre": "Parque Nacional de Komodo", "pais": "Indonesia", "tipo": "natural"},
    {"nombre": "Río Amazonas", "pais": "Varios", "tipo": "natural"},
]

# Agregar nodos al grafo con las maravillas
for maravilla in maravillas:
    G.add_node(maravilla["nombre"], pais=maravilla["pais"], tipo=maravilla["tipo"])

# Agregar aristas con distancias entre maravillas del mismo tipo
for i in range(len(maravillas)):
    for j in range(i + 1, len(maravillas)):
        maravilla1 = maravillas[i]["nombre"]
        maravilla2 = maravillas[j]["nombre"]
        tipo1 = maravillas[i]["tipo"]
        tipo2 = maravillas[j]["tipo"]

        # Agregar la arista solo si son del mismo tipo
        if tipo1 == tipo2:
            distancia = 1  # Podría ser la distancia real entre las maravillas
            G.add_edge(maravilla1, maravilla2, distancia=distancia)

# Árbol de expansión mínima para maravillas arquitectónicas
arbol_expansion_minima_arquitectonicas = nx.minimum_spanning_tree(G.subgraph([maravilla["nombre"] for maravilla in maravillas if maravilla["tipo"] == "arquitectonica"]))
print("Árbol de expansión mínima para maravillas arquitectónicas:")
print(arbol_expansion_minima_arquitectonicas.edges())

# Árbol de expansión mínima para maravillas naturales
arbol_expansion_minima_naturales = nx.minimum_spanning_tree(G.subgraph([maravilla["nombre"] for maravilla in maravillas if maravilla["tipo"] == "natural"]))
print("Árbol de expansión mínima para maravillas naturales:")
print(arbol_expansion_minima_naturales.edges())

# Determinar si existen países con maravillas arquitectónicas y naturales
paises_arquitectonicas = set([maravilla["pais"] for maravilla in maravillas if maravilla["tipo"] == "arquitectonica"])
paises_naturales = set([maravilla["pais"] for maravilla in maravillas if maravilla["tipo"] == "natural"])
paises_comunes = paises_arquitectonicas.intersection(paises_naturales)

print("Países con maravillas arquitectónicas:")
print(paises_arquitectonicas)
print("Países con maravillas naturales:")
print(paises_naturales)
print("Países con ambas maravillas:")
print(paises_comunes)

# Determinar si algún país tiene más de una maravilla del mismo tipo
paises_con_mas_de_una_arquitectonica = [pais for pais in paises_arquitectonicas if sum([1 for maravilla in maravillas if maravilla["pais"] == pais and maravilla["tipo"] == "arquitectonica"]) > 1]
paises_con_mas_de_una_natural = [pais for pais in paises_naturales if sum([1 for maravilla in maravillas if maravilla["pais"] == pais and maravilla["tipo"] == "natural"]) > 1]

print("Países con más de una maravilla arquitectónica:")
print(paises_con_mas_de_una_arquitectonica)
print("Países con más de una maravilla natural:")
print(paises_con_mas_de_una_natural)
