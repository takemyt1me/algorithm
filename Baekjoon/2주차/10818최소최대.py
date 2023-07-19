N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min = arr[0]
max = arr[N-1]
print('%d %d' %(min, max))