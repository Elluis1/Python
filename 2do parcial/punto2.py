from classGraph import Graph
from random import randint

#crea el grafo
personajesGraph = Graph(False)

# lista de personajes
personajes = [
    'luke skywalker',
    'darth vader', 'yoda',
    'boba fett',
    'c-3po',
    'leia',
    'rey',
    'kylo ren',
    'chewbacca',
    'han solo',
    'r2-d2',
    'bb-8'
]

#insertar personajes como vertices en el grafo
for character in personajes:
    personajesGraph.insert_vertice(character)


# A) y D) inserta las aristas y los capitulos estan hechos con randint
personajesGraph.insert_arist('luke skywalker', 'darth vader', randint(1, 10))
personajesGraph.insert_arist('darth vader', 'yoda', randint(1, 10))
personajesGraph.insert_arist('yoda', 'boba fett', randint(1, 10))
personajesGraph.insert_arist('boba fett', 'c-3po', randint(1, 10))
personajesGraph.insert_arist('c-3po', 'leia', randint(1, 10))
personajesGraph.insert_arist('leia', 'rey', randint(1, 10))
personajesGraph.insert_arist('rey', 'kylo ren', randint(1, 10))
personajesGraph.insert_arist('kylo ren', 'chewbacca', randint(1, 10))
personajesGraph.insert_arist('chewbacca', 'han solo', randint(1, 10))
personajesGraph.insert_arist('han solo', 'r2-d2', randint(1, 10))
personajesGraph.insert_arist('r2-d2', 'bb-8', randint(1, 10))
personajesGraph.insert_arist('bb-8', 'luke skywalker', randint(1, 10))

# B) arbol de expansion minima

[ kruskal ] = personajesGraph.kruskal()

print(kruskal)
# busqueda de yoda
if kruskal.find('yoda') != -1:
    print('Yoda es parte del árbol de expansión mínimo')
else:
    print('Yoda no es parte del árbol de expansión mínimo')

# c) 
for i in personajesGraph.size():
    vertice = personajesGraph.get_element_by_index(i)
    aristas = vertice[1]
    for j in aristas.size():
        0
