N=5
a=[1,2,3,4,5]

i1=0

encontrar=int(input("Qué número quiere encontrar?"))

i2=-1
66
for i in a:
    i2=i2+1
    if encontrar == i:
        print(f"Se encontró {encontrar}")
        break
    elif i2==4:
        print(f"No se encontró {encontrar}")
