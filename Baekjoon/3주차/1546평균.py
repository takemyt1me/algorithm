n = int(input())
score = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += score[i]/max(score)*100

print(sum/n)