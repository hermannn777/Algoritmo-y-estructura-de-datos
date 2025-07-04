def productoEscalarConInverso(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def invertirArreglo(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])
    return b


def productoEscalarConInverso(a, b):
    bInvertido = invertirArreglo(b)
    return productoEscalar(a, bInvertido)

a = [1, 2, 3]
b = [4, 5, 6]
print("El resultado entre el arreglo A y el B inverso es:", productoEscalarConInverso(a, b))