matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

numero_max = -1 
fila = 0 
columna = 0 
for i in range(len(matriz)):
    for j in range(len(matriz[i])): # <-- ¡Aquí está el cambio!
        if matriz[i][j] > numero_max:
            numero_max = matriz[i][j]
            columna = j + 1
            fila = i + 1

print(f"El número máximo es: {numero_max}")
print(f"La posición del número máximo es fila {fila} y columna {columna}")