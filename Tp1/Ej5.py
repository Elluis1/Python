def convertir_romano_a_decimal_recursivo(num_romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(num_romano) == 1:
        # Caso base: sólo queda un dígito romano en la cadena
        return valores[num_romano]

    if valores[num_romano[0]] < valores[num_romano[1]]:
        # Caso recursivo 1: el dígito actual es menor que el siguiente, se resta su valor
        return -valores[num_romano[0]] + convertir_romano_a_decimal_recursivo(num_romano[1:])
    else:
        # Caso recursivo 2: el dígito actual es mayor o igual que el siguiente, se suma su valor
        return valores[num_romano[0]] + convertir_romano_a_decimal_recursivo(num_romano[1:])

numero_romano = "MCMXCVI"
numero_decimal = convertir_romano_a_decimal_recursivo(numero_romano)
print(f"{numero_romano} en decimal es {numero_decimal}")