def busquedaL(a, valor):
    for i in range(len(a)):
        if a[i] == valor:
            return i
    return "no encontrado"

numeros = [5, 10, 15, 20]
print("resultado de busqueda lineal (buscando 15):", busquedaL(numeros, 15)) 
print("resultado de busqueda lineal (buscando 99):", busquedaL(numeros, 99)) 