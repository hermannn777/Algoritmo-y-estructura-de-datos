matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

for fila in matriz:
    print(fila)

UNO = int(input("Elija una columna: "))
columnaUNO = UNO - 1

DOS = int(input("Elija la columna por la que quiere intercambiar la primera: "))
columnaDOS = DOS - 1

if 0 <= columnaUNO < len(matriz[0]) and 0 <= columnaDOS < len(matriz[0]):
    if columnaUNO == columnaDOS:
        print("Elija columnas diferentes")
    else:
        for i in range(len(matriz)):
            matriz[i][columnaUNO], matriz[i][columnaDOS] = matriz[i][columnaDOS], matriz[i][columnaUNO]

        print("Matriz modificada:")
        for fila in matriz:
            print(fila)
else:
    print("No hay tantas columnas")