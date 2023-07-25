N = int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

pado = [0]*101
pado[1:7]=[1,1,1,2,2,3]


for i in range(7,101):
    pado[i]=pado[i-1]+pado[i-5]

for i in range(N):
    print(pado[arr[i]])

