matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

print("[1, 2, 8]")
print("[3, 4, 5]")
print("[9, 7, 6]")

numeroElegido = int(input("Elija una columna: "))
columnaElegida = numeroElegido - 1

if 0 <= columnaElegida < len(matriz):
    maximo = matriz[0][columnaElegida]
    fila_max = 0
    for i in range(len(matriz)):
     if matriz[i][columnaElegida] > maximo:
        maximo = matriz[i][columnaElegida]
        fila_max = i 
    print(f"La fila que contiene el mayor número de la columna {columnaElegida + 1} es la fila {fila_max + 1}")
else:
    print("La columna seleccionada no existe")