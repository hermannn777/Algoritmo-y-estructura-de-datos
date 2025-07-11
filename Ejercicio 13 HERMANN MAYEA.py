def rotar_derecha(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    ultimo = matriz[filas - 1][columnas - 1]

    for i in range(filas - 1, -1, -1):
        for j in range(columnas - 1, -1, -1):
            if j == 0:
                if i != 0:
                    matriz[i][j] = matriz[i - 1][columnas - 1]
                else:
                    matriz[i][j] = ultimo
            else:
                matriz[i][j] = matriz[i][j - 1]


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotar_derecha(matriz)

for fila in matriz:
    print(fila)