def sumar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    
    return resultado

matriz1 = [
    [1.5, 2.0],
    [3.2, 4.1]
]

matriz2 = [
    [5.0, 6.5],
    [7.3, 8.4]
]

suma = sumar_matrices(matriz1, matriz2)

for fila in suma:
    print(fila)
