matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

numero_max = -1 
fila = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])): # <-- ¡Aquí está el cambio!
        if matriz[i][j] > numero_max:
            numero_max = matriz[i][j]
            fial = j

print(f"El número máximo en la matriz es: {numero_max}")
print(f"Se encuentra en la columna: {fila}")