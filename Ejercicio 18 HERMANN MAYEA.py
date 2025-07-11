def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = []
    for j in range(columnas):
        fila = []
        for i in range(filas):
            fila.append(matriz[i][j])
        transpuesta.append(fila)
    
    return transpuesta


matriz = [
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0]
]

t = transponer_matriz(matriz)

for fila in t:
    print(fila)
