from classBinaryTree import BinaryTree, NodeTree

nombreArb = BinaryTree()
numPokedexArb = BinaryTree()
tiposArb = BinaryTree()

pokemonList = [
    { 'nombre': 'bulbasaur', 'pokedexNum': 1, 'tipos': ['planta', 'poison'] },
    { 'nombre': 'charmander', 'pokedexNum': 4, 'tipos': ['fuego']},
    { 'nombre': 'pidgey', 'pokedexNum': 16, 'tipos': ['normal', 'flying']},
    { 'nombre': 'pikachu', 'pokedexNum': 25, 'tipos': ['electrico'] },
    { 'nombre': 'jolteon', 'pokedexNum': 135, 'tipos': ['electrico'] },
    { 'nombre': 'lycanroc', 'pokedexNum': 745, 'tipos': ['rock'] },
    { 'nombre': 'tyrantrum', 'pokedexNum': 697, 'tipos': ['rock', 'dragon'] }
]

# A)
for pokemon in pokemonList:
    nombre = pokemon['nombre']
    pokedexNum = pokemon['pokedexNum']
    tipos = pokemon['tipos']

    nombreArb.insert_node(nombre, pokemon)
    numPokedexArb.insert_node(pokedexNum, pokemon)
    tiposArb.insert_node(tipos, pokemon)

# B)
def searchByCoincidence(node: NodeTree):
    if node.value.find('bul'.lower()) != -1:
        print(node.value)

# nombreArb.inorden(searchByCoincidence)

# C)
tipos = ['agua', 'fuego', 'planta', 'electrico']

def searchByTypes(node: NodeTree):
    for specificType in tipos:
        if specificType in node.value:
            print(node.other_values['nombre'])

 # tiposArb.inorden(searchByTypes)

# D)
# numPokedexArb.inorden()
# nombreArb.inorden()
# nombreArb.by_level()

# E)
print('buscaste a:', nombreArb.search('lycanroc').value)
print('buscaste a:', nombreArb.search('tyrantrum').value)
print('buscaste a:', nombreArb.search('jolteon').value)

# F)
tipos = ['electrico', 'steel']

def countByType(node: NodeTree, value):
    for specificType in tipos:
        if specificType in node.value:
            return 1
        else:
            return 0

# print(tiposArb.count('', countByType))
