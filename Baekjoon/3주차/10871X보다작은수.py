N, X = map(int, input().split())
arr = list(map(int, input().split()))
res = []

for i in range(N):
    if arr[i]<X:
        res.append(arr[i])

for i in res:
    print(i, end=' ')