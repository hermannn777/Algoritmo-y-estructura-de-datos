matriz = [
    [-1, 2, 8],  
    [3, -4, 5],
    [-9, 7, -6]
]
PIPO = 0
for i in matriz:
    for numero in i:
        if numero > 0:
         PIPO = PIPO + 1
print (f"Números positivos: {PIPO}")
