N, K = map(int,input().split())
length = [0]

for i in range(1, N+1):
    tmp = len(str(i))
    length.append(tmp)

def binary_search(array, target, start, end):
    while start<=end: #start와 end가 같아진 후 한 번 더 돌면 탈출
        mid = (start + end)//2

        if sum(array[:mid+1])<target:
            start = mid+1
        else:
            end = mid -1

        return start #start 인뎃스의 정수 안 숫자가 찾는 숫자

#K<=sum(length[:start+1]), == 성립시 마지막 숫자, <성립 시 앞의 숫자

res = binary_search(length, K, 1, len(length)) 

if sum(length[:res+1]) == K:
    tmp = str(length[res])
    print(tmp[len(tmp)-1])

else:
    K= K - sum(length[:res])
    tmp = str(length[res])
    print(tmp[K-1])