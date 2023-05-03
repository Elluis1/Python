class Pila():
    """Stack class"""

def crear_pila():
    return []

def pila_vacia(pila):
    return len(pila) == 0

def agregar_a_pila(pila, elemento):
    pila.append(elemento)

def sacar_de_pila(pila):
    if not pila_vacia(pila):
        return pila.pop()

def tamano_de_pila(pila):
    return len(pila)

def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

