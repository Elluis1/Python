class Criatura:
    def __init__(self, nombre, derrotador=None, descripcion=None):
        self.nombre = nombre
        self.derrotador = derrotador
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

def insertar_criatura(raiz, criatura):
    if raiz is None:
        return criatura
    if criatura.nombre < raiz.nombre:
        raiz.izquierda = insertar_criatura(raiz.izquierda, criatura)
    else:
        raiz.derecha = insertar_criatura(raiz.derecha, criatura)
    return raiz

def buscar_criatura(raiz, nombre):
    if raiz is None:
        return None
    if nombre == raiz.nombre:
        return raiz
    if nombre < raiz.nombre:
        return buscar_criatura(raiz.izquierda, nombre)
    return buscar_criatura(raiz.derecha, nombre)

def listar_inorden(raiz):
    if raiz is not None:
        listar_inorden(raiz.izquierda)
        print(f"{raiz.nombre} (Derrotada por: {raiz.derrotador if raiz.derrotador else 'Nadie'})")
        listar_inorden(raiz.derecha)

# Crear el árbol y agregar las criaturas
arbol = None

arbol = insertar_criatura(arbol, Criatura("Cerbero", "Heracles"))
arbol = insertar_criatura(arbol, Criatura("Toro de Creta", "Heracles"))
arbol = insertar_criatura(arbol, Criatura("Cierva Cerinea", "Heracles"))
arbol = insertar_criatura(arbol, Criatura("Jabalí de Erimanto", "Heracles"))
arbol = insertar_criatura(arbol, Criatura("Heracles"))
arbol = insertar_criatura(arbol, Criatura("Basilisco"))
arbol = insertar_criatura(arbol, Criatura("Sirenas"))
arbol = insertar_criatura(arbol, Criatura("Aves del Estínfalo", "Heracles"))
arbol = insertar_criatura(arbol, Criatura("Ladón"))

# Lista de criaturas y sus derrotadores
criaturas_data = [
    "1 ceto",
    "1 tifon - 2 zeus",
    "1 Equidna - 2 argos panoptes",
    "1 dino",
    "1 pefredo",
    "1 Enio",
    "1 Escila",
    "1 Caribdis",
    "1 Euriale",
    "1 Esteno",
    "1 Medusa 2 Perseo",
    "1 Ladón 2 Heracles",
    "1 Aguila del Caucaso",
    "1 quimera 2 belerofonte",
    "1 hidra de lerna 2 heracles",
    "1 leon de nemea 2 heracles",
    "1 Esfinge 2 Edipo",
    "1 Dragon de la colquida",
    "1 cerbero",
    "1 cerda de cromion 2 teseo",
    "1 ortro 2 heracles",
    "1 toro de creta 2 Teseo",
    "1 jabali de calidon 2 Atalanta",
    "1 garcinos",
    "1 gerion 2 heracles",
    "1 cloto",
    "1 laquesis",
    "1 atropos",
    "1 minotauro de creta 2 Teseo",
    "1 harpias",
    "1 argos panoptes 2 hermes",
    "1 aves del estinfalo",
    "1 talos 2 Medea",
    "1 sirenas",
    "1 piton 2 apolo",
    "1 cierva de cerinea",
    "1 basilisco",
    "1 jabali de erimanto"
]

# Adaptar la lista de criaturas y agregar al árbol
for criatura_info in criaturas_data:
    partes = criatura_info.split(" ")
    nombre_criatura = partes[1]
    derrotador = None
    
    if len(partes) > 2:
        if partes[2] == "2":
            derrotador = partes[3]
    
    criatura = Criatura(nombre_criatura, derrotador)
    arbol = insertar_criatura(arbol, criatura)

# Resto del código sigue igual

# Consultas
print("a. Listado inorden de las criaturas y quienes las derrotaron:")
listar_inorden(arbol)

# Resto del código sigue igual

# Modificar el nombre de una criatura
ladon = buscar_criatura(arbol, "Ladón")
if ladon:
    ladon.nombre = "Dragón Ladón"

# Asignar derrotador a las criaturas
cerbero = buscar_criatura(arbol, "Cerbero")
toro = buscar_criatura(arbol, "Toro de Creta")
cierva = buscar_criatura(arbol, "Cierva Cerinea")
jabali = buscar_criatura(arbol, "Jabalí de Erimanto")
aves = buscar_criatura(arbol, "Aves del Estínfalo")
if cerbero and toro and cierva and jabali and aves:
    cerbero.derrotador = "Heracles"
    toro.derrotador = "Heracles"
    cierva.derrotador = "Heracles"
    jabali.derrotador = "Heracles"
    aves.derrotador = "Heracles"

# Realizar una búsqueda por coincidencia
def buscar_coincidencia(raiz, palabra):
    resultados = []
    if raiz is not None:
        resultados += buscar_coincidencia(raiz.izquierda, palabra)
        if palabra in raiz.nombre:
            resultados.append(raiz)
        resultados += buscar_coincidencia(raiz.derecha, palabra)
    return resultados

# Eliminar criaturas
def eliminar_criatura(raiz, nombre):
    if raiz is None:
        return raiz
    if nombre < raiz.nombre:
        raiz.izquierda = eliminar_criatura(raiz.izquierda, nombre)
    elif nombre > raiz.nombre:
        raiz.derecha = eliminar_criatura(raiz.derecha, nombre)
    else:
        if raiz.izquierda is None:
            return raiz.derecha
        elif raiz.derecha is None:
            return raiz.izquierda
        raiz.nombre = criatura_minima(raiz.derecha)
        raiz.derecha = eliminar_criatura(raiz.derecha, raiz.nombre)
    return raiz

# Encontrar el valor mínimo de un árbol
def criatura_minima(raiz):
    current = raiz
    while current.izquierda:
        current = current.izquierda
    return current.nombre

# Listar criaturas no derrotadas
def listar_no_derrotadas(raiz):
    if raiz is not None:
        listar_no_derrotadas(raiz.izquierda)
        if raiz.derrotador is None:
            print(f"{raiz.nombre} (No derrotada)")
        listar_no_derrotadas(raiz.derecha)

# Listar criaturas derrotadas por un héroe
def listar_derrotadas_por(raiz, heroe):
    if raiz is not None:
        listar_derrotadas_por(raiz.izquierda, heroe)
        if raiz.derrotador == heroe:
            print(f"{raiz.nombre}")
        listar_derrotadas_por(raiz.derecha, heroe)

# Listar héroes o dioses con mayor cantidad de derrotas
def listar_top_derrotadores(raiz):
    derrotadores = {}

    def contar_derrotadores(raiz):
        if raiz is not None:
            contar_derrotadores(raiz.izquierda)
            if raiz.derrotador:
                if raiz.derrotador in derrotadores:
                    derrotadores[raiz.derrotador] += 1
                else:
                    derrotadores[raiz.derrotador] = 1
            contar_derrotadores(raiz.derecha)

    contar_derrotadores(raiz)

    top_derrotadores = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas son:")
    for derrotador, cantidad in top_derrotadores:
        print(f"{derrotador} - {cantidad} criaturas")

# Realizar un listado por nivel del árbol
def listar_por_nivel(raiz):
    if raiz is not None:
        niveles = [[raiz]]
        while niveles:
            nivel_actual = niveles.pop(0)
            for criatura in nivel_actual:
                print(criatura.nombre, end=" ")
            print()
            nivel_siguiente = []
            for criatura in nivel_actual:
                if criatura.izquierda:
                    nivel_siguiente.append(criatura.izquierda)
                if criatura.derecha:
                    nivel_siguiente.append(criatura.derecha)
            if nivel_siguiente:
                niveles.append(nivel_siguiente)

# Cargar descripciones de criaturas
cerbero.descripcion = "Criatura mitológica de tres cabezas que guarda la entrada del Hades."
toro.descripcion = "Un toro monstruoso que fue domesticado por Heracles como uno de sus trabajos."
cierva.descripcion = "Una cierva dorada que era sagrada para Artemis, la diosa de la caza."
jabali.descripcion = "Un jabalí feroz de Erimanto que Heracles cazó como uno de sus trabajos."
aves.descripcion = "Aves carnívoras que infestaban el Lago Estínfalo y fueron derrotadas por Heracles."

# Consultas
print("a. Listado inorden de las criaturas y quienes las derrotaron:")
listar_inorden(arbol)

print("\nb. Breve descripción de cada criatura:")
for criatura in [cerbero, toro, cierva, jabali, aves]:
    print(f"{criatura.nombre}: {criatura.descripcion}")

print("\nc. Información de la criatura Talos:")
talos = buscar_criatura(arbol, "Talos")
if talos:
    print(f"Nombre: {talos.nombre}")
    print(f"Derrotada por: {talos.derrotador}")
    print(f"Descripción: {talos.descripcion}")

print("\nd. Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
listar_top_derrotadores(arbol)

print("\ne. Criaturas derrotadas por Heracles:")
listar_derrotadas_por(arbol, "Heracles")

print("\nf. Criaturas no derrotadas:")
listar_no_derrotadas(arbol)

print("\ng. Campo 'capturada' de cada criatura:")
listar_inorden(arbol)

print("\nh. Modificar nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto:")
cerbero.derrotador = "Heracles"
toro.derrotador = "Heracles"
cierva.derrotador = "Heracles"
jabali.derrotador = "Heracles"
print("Nodos actualizados.")

print("\i. Búsqueda por coincidencia:")
coincidencias = buscar_coincidencia(arbol, "Heracles")
for criatura in coincidencias:
    print(criatura.nombre)

print("\nj. Eliminar al Basilisco y a las Sirenas:")
arbol = eliminar_criatura(arbol, "Basilisco")
arbol = eliminar_criatura(arbol, "Sirenas")
print("Basilisco y Sirenas eliminadas.")

print("\nk. Modificar el nodo que contiene a las Aves del Estínfalo:")
aves.descripcion += " Heracles las derrotó como uno de sus trabajos."
print("Nodo actualizado.")

print("\nl. Modificar el nombre de la criatura Ladón:")
print("Nombre de la criatura Ladón ya fue modificado a 'Dragón Ladón'.")

print("\nm. Listado por nivel del árbol:")
listar_por_nivel(arbol)
