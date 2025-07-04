def busquedaB(a, valor):
    izq = 0
    der = len(a) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if a[medio] == valor:
            return medio
        if a[medio] < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return "no encontrado"


ordenados = [1, 3, 5, 7, 9]
print("resultado de busqueda binaria (buscando 5):", busquedaB(ordenados, 5)) 
print("resultado de busqueda binaria (buscando 8):", busquedaB(ordenados, 8))  