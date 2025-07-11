matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

print("[1, 2, 8]")
print("[3, 4, 5]")
print("[9, 7, 6]")
numeroElegido = 1
fila = 0 
columna = 0 
booleano = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == numeroElegido:
            columna = j + 1
            fila = i + 1
            print(f"Este número se encuentra en la fila {fila} y la columna {columna}")
            booleano = True

if not booleano:
    print("El número no se encuentra en esta matriz")