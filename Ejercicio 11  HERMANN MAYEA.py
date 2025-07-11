matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

for variable in matriz:
    print(variable)

UNO = int(input("Elija una fila: "))
filaUNO = UNO - 1

DOS = int(input("Elija la fila por la que quiere intercambiar la primera: "))
filaDOS = DOS - 1

if 0 <= filaUNO < len(matriz) and 0 <= filaDOS < len(matriz):
    if filaUNO == filaDOS:
        print("Elija filas diferentes")
    else:
        matriz[filaUNO], matriz[filaDOS] = matriz[filaDOS], matriz[filaUNO]
        print("Matriz modificada:")
        for fila in matriz:
            print(fila)
else:
    print("No hay tantas filas")