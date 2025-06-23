A1=[5,10,15,20,25]
A2=[7,14,21,28,35]
A3=[]

i=0

for i in range(5):
    if i %2==0:
        A3.append(A1[i])
    elif i%2==1:
        A3.append(A2[i])
print(A3)