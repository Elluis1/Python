def usar_la_fuerza(mochila, objetos_sacados=0):
    """
    Función recursiva para buscar un sable de luz en una mochila Jedi.
    Devuelve la cantidad de objetos sacados antes de encontrar el sable de luz,
    o -1 si no se encontró el sable de luz en la mochila.
    """
    if len(mochila) == 0:
        # Caso base: no quedan objetos en la mochila
        return -1

    objeto = mochila.pop(0)  # Sacar el primer objeto de la mochila
    if objeto == "sable de luz":
        # Caso base: se encontró el sable de luz
        return objetos_sacados

    # Caso recursivo: seguir buscando en la mochila
    return usar_la_fuerza(mochila, objetos_sacados + 1)

mochila = ["agua", "sable de luz", "brújula"]
objetos_sacados = usar_la_fuerza(mochila)
if objetos_sacados == -1:
    print("No se encontró el sable de luz en la mochila.")
else:
    print(f"Se encontró el sable de luz después de sacar {objetos_sacados} objetos.")