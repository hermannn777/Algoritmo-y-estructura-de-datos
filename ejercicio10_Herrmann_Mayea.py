def ordenar(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

valores = [100, 20, 7, 11]
print("arreglo ordenado en forma ascendente:", ordenar(valores))