N, K = map(int, input().split())
line =[]
for _ in range(N):
    line.append(int(input()))

start=1
end= max(line)

#res = [] 
while start<=end: #start와 end가 같아지는 순간 탈출
    mid = (start+end)//2
    sum = 0
    for i in range(N):
        sum += line[i]//mid
    
    if sum < K:
        end = mid -1
    
    else:
        #res.append(mid)
        start = mid +1
    
print(end)
#print(max(res))
