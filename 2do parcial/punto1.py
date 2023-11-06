class Pokemon:
    def __init__(self, number, name, types):
        self.number = number
        self.name = name
        self.types = types

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            return Node(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search_by_name_prefix(self, prefix):
        result = []
        self._search_by_name_prefix(self.root, prefix, result)
        return result

    def _search_by_name_prefix(self, node, prefix, result):
        if node is not None:
            if node.data.name.startswith(prefix):
                result.append(node.data)
            if prefix < node.key:
                self._search_by_name_prefix(node.left, prefix, result)
            self._search_by_name_prefix(node.right, prefix, result)

    def get_names_by_type(self, type_name):
        result = []
        self._get_names_by_type(self.root, type_name, result)
        return result

    def _get_names_by_type(self, node, type_name, result):
        if node is not None:
            if type_name in node.data.types:
                result.append(node.data.name)
            self._get_names_by_type(node.left, type_name, result)
            self._get_names_by_type(node.right, type_name, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)

class PokemonData:
    def __init__(self):
        self.pokemons = [
            Pokemon(1, "Bulbasaur", ["Planta", "Veneno"]),
            Pokemon(4, "Charmander", ["Fuego"]),
            Pokemon(7, "Squirtle", ["Agua"]),
            Pokemon(25, "Pikachu", ["Electrico"]),
            Pokemon(131, "Lapras", ["Agua", "Hielo"]),
            Pokemon(697, "Tyrantrum", ["Roca", "Dragon"]),
            Pokemon(135, "Jolteon", ["Electrico"]),
            Pokemon(745, "Lycanroc", ["Roca"])
        ]

    def load_pokemon_data(self, file_name):
        # Este método se mantiene para compatibilidad pero no hace nada con la lista incorporada
        pass

if __name__ == "__main__":
    data = PokemonData()

    number_tree = BinaryTree()
    name_tree = BinaryTree()
    type_tree = BinaryTree()

    for pokemon in data.pokemons:
        number_tree.insert(pokemon.number, pokemon)
        name_tree.insert(pokemon.name, pokemon)
        for t in pokemon.types:
            type_tree.insert(t, pokemon)

    print("Buscar Pokémon por número:")
    number = 25  # Número del Pokémon a buscar
    result = number_tree.search(number)
    if result:
        print(f"Pokemon número {number}: {result.data.name} - Tipo(s): {', '.join(result.data.types)}")
    else:
        print(f"No se encontró ningún Pokémon con el número {number}")

    print("\nBuscar Pokémon por nombre (por proximidad):")
    name_prefix = "Bul"  # Prefijo del nombre a buscar
    result = name_tree.search_by_name_prefix(name_prefix)
    if result:
        print(f"Resultados para nombres que comienzan con '{name_prefix}':")
        for pokemon in result:
            print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")
    else:
        print(f"No se encontró ningún Pokémon cuyo nombre comience con '{name_prefix}'")

    print("\nNombres de Pokémon por tipo:")
    type_name = "Agua"  # Tipo de Pokémon a buscar
    result = type_tree.get_names_by_type(type_name)
    if result:
        print(f"Nombres de Pokémon de tipo '{type_name}':")
        for name in result:
            print(name)
    else:
        print(f"No se encontraron Pokémon de tipo '{type_name}'")

    print("\nListado en orden ascendente por número:")
    ascending_number_list = number_tree.in_order_traversal()
    for pokemon in ascending_number_list:
        print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")

    print("\nListado en orden alfabético por nombre:")
    name_list = name_tree.in_order_traversal()
    for pokemon in name_list:
        print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")

    # Al final la busqueda de los pokemon especificos
    # me simplifique utilizando la busqueda por proximidad
    name_jol = "Jol"
    result = name_tree.search_by_name_prefix(name_jol)
    if result:
        print("\nEstos son los datos de Jolteon:")
        for pokemon in result:
            print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")
    else:
        print(f"No se encontró a Jolteon")

    name_tyr = "Tyr"
    result = name_tree.search_by_name_prefix(name_tyr)
    if result:
        print("\nEstos son los datos de Jolteon:")
        for pokemon in result:
            print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")
    else:
        print(f"No se encontró a Tyrantrum")

    name_lyc = "Lyc"
    result = name_tree.search_by_name_prefix(name_lyc)
    if result:
        print("\nEstos son los datos de Lycanroc:")
        for pokemon in result:
            print(f"{pokemon.number}: {pokemon.name} - Tipo(s): {', '.join(pokemon.types)}")
    else:
        print("\nNo se encontró a Lycanroc")
