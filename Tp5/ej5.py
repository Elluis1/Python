class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None

class ArbolMCU:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        self.raiz = self._insertar(self.raiz, nombre, es_heroe)

    def _insertar(self, nodo, nombre, es_heroe):
        if nodo is None:
            return Nodo(nombre, es_heroe)
        
        if nombre < nodo.nombre:
            nodo.izquierda = self._insertar(nodo.izquierda, nombre, es_heroe)
        else:
            nodo.derecha = self._insertar(nodo.derecha, nombre, es_heroe)
        
        return nodo

    def listar_villanos_ordenados(self):
        return self._listar_villanos_ordenados(self.raiz)

    def _listar_villanos_ordenados(self, nodo):
        if nodo is None:
            return []
        
        villanos = []
        if not nodo.es_heroe:
            villanos.append(nodo.nombre)
        
        villanos.extend(self._listar_villanos_ordenados(nodo.izquierda))
        villanos.extend(self._listar_villanos_ordenados(nodo.derecha))
        
        return sorted(villanos)

    def superheroes_con_C(self):
        return self._superheroes_con_C(self.raiz)

    def _superheroes_con_C(self, nodo):
        if nodo is None:
            return []
        
        heroes = []
        if nodo.es_heroe and nodo.nombre.startswith("C"):
            heroes.append(nodo.nombre)
        
        heroes.extend(self._superheroes_con_C(nodo.izquierda))
        heroes.extend(self._superheroes_con_C(nodo.derecha))
        
        return heroes

    def contar_superheroes(self):
        return self._contar_superheroes(self.raiz)

    def _contar_superheroes(self, nodo):
        if nodo is None:
            return 0
        
        count = 0
        if nodo.es_heroe:
            count = 1
        
        count += self._contar_superheroes(nodo.izquierda)
        count += self._contar_superheroes(nodo.derecha)
        
        return count

    def buscar_y_modificar(self, nombre_buscar, nuevo_nombre):
        self.raiz = self._buscar_y_modificar(self.raiz, nombre_buscar, nuevo_nombre)

    def _buscar_y_modificar(self, nodo, nombre_buscar, nuevo_nombre):
        if nodo is None:
            return None
        
        if nodo.nombre == nombre_buscar:
            nodo.nombre = nuevo_nombre
        
        nodo.izquierda = self._buscar_y_modificar(nodo.izquierda, nombre_buscar, nuevo_nombre)
        nodo.derecha = self._buscar_y_modificar(nodo.derecha, nombre_buscar, nuevo_nombre)
        
        return nodo

    def listar_superheroes_descendente(self):
        return sorted(self._listar_superheroes_descendente(self.raiz), reverse=True)

    def _listar_superheroes_descendente(self, nodo):
        if nodo is None:
            return []
        
        heroes = []
        if nodo.es_heroe:
            heroes.append(nodo.nombre)
        
        heroes.extend(self._listar_superheroes_descendente(nodo.izquierda))
        heroes.extend(self._listar_superheroes_descendente(nodo.derecha))
        
        return heroes

def crear_bosque(arbol_mcu):
    superheroes = ArbolMCU()
    villanos = ArbolMCU()

    def crear_bosque_recursivo(nodo):
        if nodo is None:
            return

        if nodo.es_heroe:
            superheroes.insertar(nodo.nombre, True)
        else:
            villanos.insertar(nodo.nombre, False)

        crear_bosque_recursivo(nodo.izquierda)
        crear_bosque_recursivo(nodo.derecha)

    crear_bosque_recursivo(arbol_mcu.raiz)

    return superheroes, villanos

def contar_nodos(arbol):
    def _contar_nodos_recursivo(nodo):
        if nodo is None:
            return 0

        return 1 + _contar_nodos_recursivo(nodo.izquierda) + _contar_nodos_recursivo(nodo.derecha)

    return _contar_nodos_recursivo(arbol.raiz)

def barrido_ordenado_alfabeticamente(arbol):
    def _barrido_ordenado_alfabeticamente_recursivo(nodo):
        if nodo is None:
            return []

        elementos = []
        elementos.extend(_barrido_ordenado_alfabeticamente_recursivo(nodo.izquierda))
        elementos.append(nodo.nombre)
        elementos.extend(_barrido_ordenado_alfabeticamente_recursivo(nodo.derecha))

        return elementos

    return _barrido_ordenado_alfabeticamente_recursivo(arbol.raiz)

# Ejemplo de uso:

arbol_mcu = ArbolMCU()
arbol_mcu.insertar("Iron Man", True)
arbol_mcu.insertar("Captain America", True)
arbol_mcu.insertar("Loki", False)
arbol_mcu.insertar("Thor", True)
arbol_mcu.insertar("Doctor Strange", True)
arbol_mcu.insertar("Black Widow", True)
arbol_mcu.insertar("Thanos", False)
arbol_mcu.insertar("Hulk", True)

# a. Insertar un nodo
arbol_mcu.insertar("Scarlet Witch", True)

# b. Listar villanos ordenados alfabéticamente
print(arbol_mcu.listar_villanos_ordenados())

# c. Mostrar superhéroes que empiezan con C
print(arbol_mcu.superheroes_con_C())

# d. Contar cuántos superhéroes hay en el árbol
print(arbol_mcu.contar_superheroes())

# e. Modificar el nombre de "Doctor Strange"
arbol_mcu.buscar_y_modificar("Doctor Strange", "Doctor Strange (Stephen Strange)")

# f. Listar superhéroes ordenados de manera descendente
print(arbol_mcu.listar_superheroes_descendente())

# g. Crear un bosque
superheroes, villanos = crear_bosque(arbol_mcu)

# I. Contar nodos en cada árbol
print("Superhéroes:", contar_nodos(superheroes))
print("Villanos:", contar_nodos(villanos))

# II. Barrido ordenado alfabéticamente de cada árbol
print("Superhéroes:", barrido_ordenado_alfabeticamente(superheroes))
print("Villanos:", barrido_ordenado_alfabeticamente(villanos))
