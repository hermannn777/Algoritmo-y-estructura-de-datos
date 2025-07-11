def multiplicar_matrices(m1, m2):
    filas_m1 = len(m1)
    columnas_m1 = len(m1[0])
    columnas_m2 = len(m2[0])
    
    resultado = []
    for i in range(filas_m1):
        fila = []
        for j in range(columnas_m2):
            suma = 0
            for k in range(columnas_m1):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado

matriz1 = [
    [1.0, 2.0],
    [3.0, 4.0]
]

matriz2 = [
    [5.0, 6.0],
    [7.0, 8.0]
]

producto = multiplicar_matrices(matriz1, matriz2)

for fila in producto:
    print(fila)
