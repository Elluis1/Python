def contar_palabra(palabra, vector):
    if not vector:
        return 0

    if vector[0] == palabra:
        return 1 + contar_palabra(palabra, vector[1:])
    else:
        return contar_palabra(palabra, vector[1:])

vector_palabras = ['hola', 'mundo', 'hola', 'amigo', 'hola']
palabra_buscada = 'hola'

cantidad = contar_palabra(palabra_buscada, vector_palabras)
print("La palabra", palabra_buscada, "aparece", cantidad, "veces en el vector.")
