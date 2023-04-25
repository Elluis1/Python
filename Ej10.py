def digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + digitos(n//10)
print(digitos(1123123123))
