def fraccion(num):
    if num == 0:
        return "error"
    elif num < 0:
        return 1 * 1/num
    else:
        return 1/num + 1/(num-1)

print(fraccion(7))

