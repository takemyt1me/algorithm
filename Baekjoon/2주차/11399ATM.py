N= int(input())
arr = list(map(int,input().split()))

arr.sort()
count = N
res = 0
for i in range(N):
    res += arr[i]*count
    count -=1

print(res)