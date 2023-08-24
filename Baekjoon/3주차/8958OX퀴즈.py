N = int(input())

def score(word):
    total = 0
    cnt = 1
    
    for i in range(len(word)):
        if word[i] == 'O':
            total += cnt
            cnt +=1
        else:
            cnt=1
    return total

for _ in range(N):
    words = input()
    res = score(words)

    print(res)