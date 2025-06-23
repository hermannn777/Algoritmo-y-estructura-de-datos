N=5
a=[1,2,3,4,5]
print(a)
b=[]
i=0
for i in range(N):
    b.append(a[N - (i + 1)])
print(b)