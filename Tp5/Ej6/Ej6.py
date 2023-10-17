from collections import deque

class Jedi:
    def __init__(self, nombre, especie, nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.nacimiento = nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros

class NodoJedi:
    def __init__(self, jedi):
        self.jedi = jedi
        self.izquierda = None
        self.derecha = None

class ArbolJedi:
    def __init__(self):
        self.raiz_nombre = None
        self.raiz_ranking = None
        self.raiz_especie = None

    def insertar(self, jedi):
        self.raiz_nombre = self._insertar_por_nombre(self.raiz_nombre, jedi)
        self.raiz_ranking = self._insertar_por_ranking(self.raiz_ranking, jedi)
        self.raiz_especie = self._insertar_por_especie(self.raiz_especie, jedi)

    # Funciones para el árbol por nombre
    def _insertar_por_nombre(self, nodo, jedi):
        if nodo is None:
            return NodoJedi(jedi)
        if jedi.nombre < nodo.jedi.nombre:
            nodo.izquierda = self._insertar_por_nombre(nodo.izquierda, jedi)
        else:
            nodo.derecha = self._insertar_por_nombre(nodo.derecha, jedi)
        return nodo

    def barrido_inorden_nombre(self):
        return self._barrido_inorden_nombre(self.raiz_nombre)

    def _barrido_inorden_nombre(self, nodo):
        if nodo is None:
            return []
        result = []
        result.extend(self._barrido_inorden_nombre(nodo.izquierda))
        result.append(nodo.jedi.nombre)
        result.extend(self._barrido_inorden_nombre(nodo.derecha))
        return result

    # Funciones para el árbol por ranking
    def _insertar_por_ranking(self, nodo, jedi):
        if nodo is None:
            return NodoJedi(jedi)
        if "Jedi Master" in jedi.ranking:
            if nodo.jedi.ranking and "Jedi Master" in nodo.jedi.ranking:
                if jedi.ranking.index("Jedi Master") < nodo.jedi.ranking.index("Jedi Master"):
                    nodo.izquierda = self._insertar_por_ranking(nodo.izquierda, jedi)
                else:
                    nodo.derecha = self._insertar_por_ranking(nodo.derecha, jedi)
            else:
                nodo.izquierda = self._insertar_por_ranking(nodo.izquierda, jedi)
        else:
            nodo.derecha = self._insertar_por_ranking(nodo.derecha, jedi)
        return nodo

    def barrido_inorden_ranking(self):
        return self._barrido_inorden_ranking(self.raiz_ranking)

    def _barrido_inorden_ranking(self, nodo):
        if nodo is None:
            return []
        result = []
        result.extend(self._barrido_inorden_ranking(nodo.izquierda))
        result.append(nodo.jedi.nombre)
        result.extend(self._barrido_inorden_ranking(nodo.derecha))
        return result

    # Funciones para el árbol por especie
    def _insertar_por_especie(self, nodo, jedi):
        if nodo is None:
            return NodoJedi(jedi)
        if jedi.especie < nodo.jedi.especie:
            nodo.izquierda = self._insertar_por_especie(nodo.izquierda, jedi)
        else:
            nodo.derecha = self._insertar_por_especie(nodo.derecha, jedi)
        return nodo

    def barrido_por_nivel_especie(self):
        return self._barrido_por_nivel_especie(self.raiz_especie)

    def _barrido_por_nivel_especie(self, nodo):
        if nodo is None:
            return []
        result = []
        queue = deque()
        queue.append(nodo)
        while queue:
            current = queue.popleft()
            result.append(current.jedi.nombre)
            if current.izquierda:
                queue.append(current.izquierda)
            if current.derecha:
                queue.append(current.derecha)
        return result

# Funciones para cargar los datos de los Jedi desde un archivo
def cargar_jedi_desde_archivo(archivo):
    with open(archivo, "r") as file:
        lines = file.readlines()

    jedi_data = []
    current_jedi = None

    for line in lines:
        if line.strip() == "":
            if current_jedi:
                jedi_data.append(current_jedi)
                current_jedi = None
        else:
            key, value = line.strip().split(": ")
            if key == "Nombre":
                current_jedi = Jedi(value, "", "", "", [], [])
            elif key == "Especie":
                current_jedi.especie = value
            elif key == "Año de nacimiento":
                current_jedi.nacimiento = value
            elif key == "Color de sable de luz":
                current_jedi.color_sable = value
            elif key == "Ranking":
                current_jedi.ranking = value.split(", ")
            elif key == "Maestro":
                current_jedi.maestros = value.split(", ")
    if current_jedi:
        jedi_data.append(current_jedi)
    return jedi_data

# Ejemplo de uso:

archivo = "Python\Luigi\Python\Trabajos Python\Tp5\Ej6\Jedi.txt"  # Reemplaza con la ubicación de tu archivo de datos de Jedi
jedi_data = cargar_jedi_desde_archivo(archivo)
arbol_jedi = ArbolJedi()

# Insertar los Jedi en el árbol por nombre, ranking y especie
for jedi in jedi_data:
    arbol_jedi.insertar(jedi)

# a. Mostrar una lista de Jedi ordenada alfabéticamente por nombre
lista_jedi_nombre = arbol_jedi.barrido_inorden_nombre()
print("Lista de Jedi ordenada alfabéticamente por nombre:")
for jedi in lista_jedi_nombre:
    print(jedi)

# b. Mostrar una lista de Jedi ordenada alfabéticamente por ranking
lista_jedi_ranking = arbol_jedi.barrido_inorden_ranking()
print("\nLista de Jedi ordenada alfabéticamente por ranking:")
for jedi in lista_jedi_ranking:
    print(jedi)

# c. Mostrar una lista de Jedi por nivel del árbol por especie
lista_jedi_nivel_especie = arbol_jedi.barrido_por_nivel_especie()
print("\nLista de Jedi por nivel del árbol por especie:")
for jedi in lista_jedi_nivel_especie:
    print(jedi)
