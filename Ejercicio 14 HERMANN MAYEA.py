def rotar_izquierda(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    primero = matriz[0][0]

    for i in range(filas):
        for j in range(columnas):
            if j == columnas - 1:
                if i != filas - 1:
                    matriz[i][j] = matriz[i + 1][0]
                else:
                    matriz[i][j] = primero
            else:
                matriz[i][j] = matriz[i][j + 1]


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotar_izquierda(matriz)

for fila in matriz:
    print(fila)
