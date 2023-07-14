n, m, k = map(int, input().split())
nums=[]
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)

first=nums[0]
second=nums[1]
sum =0

while True:
    for _ in range(k):
        if m==0:
            break

        sum += first
        m-=1
    
    if m==0:
        break

    sum += second
    m -=1


print(sum)



