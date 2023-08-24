N, K = map(int, input().split())
num = list(map(int, input().split()))

multi = []
count = 0

def Is_lastest(start, arr1, arr2): #arr1 = 사용 순서, arr2 = 멀티탭
    
    for i in range(len(arr1)-1, start, -1): #마지막 부터 start전까지
        if arr1[i] in arr2:
            return arr2.index(arr1[i])
    return None


for i in range(K):
    if num[i] in multi: #멀티탭 안 존재 여부
        continue

    else:
        if len(multi)<N:#아직 다 안 꽃힌 경우
            multi.append(num[i])
        else:
            if Is_lastest(i, num, multi) is None:
                multi[0] = num[i]
                count +=1
            else:
                multi[Is_lastest(i, num, multi)] = num[i]
                count+=1

print(count)

