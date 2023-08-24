word = input()
res = [0]*26

for i in range(len(word)):
    k = ord(word[i])-97

    if res[k] == 0:
        res[k] = i+1
    
for i in range(26):
    print(res[i]-1, end=' ')