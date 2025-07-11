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
    fila = matriz[filaElegida]
    maximo = fila[0]
    columna_max = 0
    for j in range(len(fila)):
     if fila[j] > maximo:
        maximo = fila[j]
        columna_max = j 
    print(f"La columna que contiene el mayor número de la fila {filaElegida + 1} es la columna {columna_max + 1}")
else:
    print("La fila seleccionada no existe")