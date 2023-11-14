from arbol import BinaryTree

class pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre=nombre
        self.numero=numero
        self.tipo=tipo
        
    def __str__(self):
        return f'{self.nombre} {self.numero} {self.tipo}'

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;

nombre_tree=BinaryTree()
pokedexNum_tree=BinaryTree()
tipos_tree=BinaryTree()

pokemon1 = pokemon("Pikachu", 25, "Eléctrico")
pokemon2 = pokemon("Bulbasaur", 1, "Planta")
pokemon3 = pokemon("Charizard", 6, "Fuego")
pokemon4 = pokemon("Squirtle", 7, "Agua")
pokemon5 = pokemon("Jigglypuff", 39, "Normal")
pokemon6 = pokemon("Vaporeon", 134, "Agua")
pokemon7 = pokemon("Mewtwo", 150, "Psíquico")
pokemon8 = pokemon("Gyarados", 130, "Agua")
pokemon9 = pokemon("Jolteon", 135, "Eléctrico")
pokemon10 = pokemon("Lycanroc", 745, "Roca")
pokemon11 = pokemon("Tyrantrum",697, "Dragón")

pokemones= [pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,pokemon7,pokemon8,pokemon9,pokemon10,pokemon11]

for pokemon in pokemones:
    nombre_tree.insert_node(pokemon.nombre,(pokemon.numero,pokemon.tipo))
    pokedexNum_tree.insert_node(pokemon.numero,(pokemon.nombre,pokemon.tipo))
    tipos_tree.insert_node(pokemon.tipo,(pokemon.nombre,pokemon.numero))
    
nombre_tree.inorden()
pokedexNum_tree.inorden()
tipos_tree.inorden()

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres;
print(' ')

# pos2=pokedexNum_tree.search(25)

# if pos2 is not None:
#     print(pos2.value,pos2.other_values)
#     info=nombre_tree.search_by_coincidence("Bul")
    
# print()

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
lista_tipo= ['Agua','Fuego','Planta','Eléctrico']

for i in lista_tipo:
    poke=tipos_tree.search(i)
    print(poke.other_values)
    
    
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print('Por orden ascendente')

nombre_tree.inorden()
print(' ')

pokedexNum_tree.inorden()
print(' ')

print('Por orden por nivel')
nombre_tree.by_level()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
lista_pokemos=['Jolteon', 'Lycanroc' , 'Tyrantrum']

for i in lista_pokemos:
    pos=nombre_tree.search(i)
    print(pos.value,pos.other_values)

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

print("De tipo Electrico hay:",tipos_tree.contar('Eléctrico'), 'pokemons')
print("De tipo Acero hay:",tipos_tree.contar('Acero'), 'pokemons')
