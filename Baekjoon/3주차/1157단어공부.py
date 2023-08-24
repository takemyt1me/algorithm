words = input()
arr = [0]*123
count = [0]*26
rep = 0
max = 0

for word in words:
    arr[ord(word)]+=1 #아스키코드로 배열에 저장

for i in range(len(count)):
    count[i] = arr[i+65]+arr[i+97] #대소문자 합친 갯수

for i in range(len(count)):
    if count[i] >=max:
        max = count[i] #최댓값 찾기
        k = i

for cnt in count:
    if cnt ==max:
        rep +=1 #최댓값 중복 여부

if rep ==1:
    print(chr(k+65))

else:
    print('?')
