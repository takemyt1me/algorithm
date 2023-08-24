N, M = map(int, input().split())
card = list(map(int, input().split()))

max = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != k and j != k and i != j:
                res = card[i]+card[j]+card[k]
                if res>max and res<=M:
                    max = res

print(max)