N = int(input())
num = list(map(int, input().split()))

mins = []
for i in range(len(num)): 
    cnt = 1
    for j in range(0, i):
        if num[i] > num[j]: #앞에 작은게 있을 경우
            cnt =0
    if cnt:
        mins.append(i)

def ascending_arr(arr):
    res_arr = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] == max(arr[:i+1]):
            res_arr.append(arr[i])
    return res_arr

res =[]
for i in range(len(mins)):
    tmp = ascending_arr(num[mins[i]:])
    if len(tmp)>len(res):
        res = tmp

print(len(res))