from classGraph import Graph
from random import randint

personajesGraph = Graph(False)

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

for character in personajes:
    personajesGraph.insert_vertice(character)

# A) y D)
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

# B)

[ kruskal ] = personajesGraph.kruskal()

print(kruskal)

if kruskal.find('yoda') != -1:
    print('Yoda es parte del árbol de expansión mínimo')
else:
    print('Yoda no es parte del árbol de expansión mínimo')
