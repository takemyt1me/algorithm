"""
def diction(word1, word2):
    res = 0
    for i in range(len(word1)):
        if word1[i]<word2[i]:
            res = 1
            break
        elif word1[i]>word2[i]:
            res = 0
            break
        else:
            continue

    return res

def swap(n1, n2):
    return n2, n1

N = int(input())
word = []
for _ in range(N):
    word.append(input())

word = list(set(word))

for i in range(len(word)):
    for j in range(len(word)):
        if len(word[i])<len(word[j]):
            word[i], word[j]=swap(word[i], word[j])
        elif len(word[i])==len(word[j]):
            if diction(word[i], word[j]) == 1:
                word[i], word[j]=swap(word[i], word[j])
            
for i in range(len(word)):
    print(word[i])
"""
N = int(input())
word = []
for _ in range(N):
    word.append(input())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in range(len(word)):
    print(word[i])