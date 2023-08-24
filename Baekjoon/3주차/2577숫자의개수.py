A = int(input())
B = int(input())
C = int(input())

nums = list(str(A*B*C))
arr = [0]*10

for num in nums:
    arr[int(num)]+=1

for i in range(10):
    print(arr[i])

    
