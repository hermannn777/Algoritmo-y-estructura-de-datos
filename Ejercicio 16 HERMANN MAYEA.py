def restar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    
    return resultado


matriz1 = [
    [5.5, 6.0],
    [7.2, 8.1]
]

matriz2 = [
    [1.0, 2.5],
    [3.3, 4.4]
]

resta = restar_matrices(matriz1, matriz2)

for fila in resta:
    print(fila)
