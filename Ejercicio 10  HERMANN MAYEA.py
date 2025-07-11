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
if 0 <= columnaElegida < len(matriz[0]):
    resultado = 0
    for i in range(len(matriz)):
        resultado = resultado + matriz[i][columnaElegida]
    print(f"La suma de los elementos de la columna {columnaElegida + 1} da como resultado: {resultado}")
else:
    print("La fila seleccionada no existe")