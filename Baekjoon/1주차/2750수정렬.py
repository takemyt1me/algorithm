n=int(input())
nums=[]
for i in range(n):
    a=int(input())
    nums.append(a)
asnums = sorted(nums)

for asnum in asnums:
    print(asnum)