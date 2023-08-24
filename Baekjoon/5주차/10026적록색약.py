N = int(input())
color = []
for _ in range(N):
    color.append(list(input()))

graph = []
value = 0
for i in range(N):
    row = []
    for j in range(N):
        row.append((value, color[i][j]))
        value+=1
    graph.append(row) #자리 번호 만들어주기

G=dict()

for i in range(N*N):
    if 
