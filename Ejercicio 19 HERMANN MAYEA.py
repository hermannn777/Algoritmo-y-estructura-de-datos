def inversa_matriz(m):
    n = len(m)
    identidad = [[float(i == j) for j in range(n)] for i in range(n)]
    matriz = [fila[:] for fila in m]
    
    for i in range(n):
        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("La matriz no tiene inversa.")
        
        for j in range(n):
            matriz[i][j] /= pivote
            identidad[i][j] /= pivote
        
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n):
                    matriz[k][j] -= factor * matriz[i][j]
                    identidad[k][j] -= factor * identidad[i][j]
    
    return identidad

matriz = [
    [4.0, 7.0],
    [2.0, 6.0]
]

inversa = inversa_matriz(matriz)

for fila in inversa:
    print(fila)
