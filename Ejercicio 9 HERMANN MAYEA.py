matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

print("[1, 2, 8]")
print("[3, 4, 5]")
print("[9, 7, 6]")

numeroElegido = int(input("Elija una fila: "))
filaElegida = numeroElegido - 1
if 0 <= filaElegida < len(matriz):
    resultado = 0
    for i in matriz[filaElegida]:
        resultado = resultado + i
    print(f"La suma de los elementos de la fila {filaElegida + 1} da como resultado: {resultado}")
else:
    print("La fila seleccionada no existe")
