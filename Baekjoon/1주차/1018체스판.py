n, m = map(int, input().split())
board=[]
count1= [[0 for j in range(m)] for i in range(n)]
count2= [[0 for j in range(m)] for i in range(n)] #count 배열 0으로 초기화

for _ in range(n):
    board.append(input())

for i in range(n):
    for j in range(m):
        if i%2 == 1: #짝수 행 WBWB..배열로 만듬
            if j%2 == 1 and board[i][j] == 'W':
                count1[i][j] = 1
            elif j%2 == 0 and board[i][j] == 'B':
                count1[i][j] = 1
        else: #홀수 행 BWBW..배열로 만듬
            if j%2 == 1 and board[i][j] == 'B':
                count1[i][j] = 1
            elif j%2 == 0 and board[i][j] == 'W':
                count1[i][j] = 1

for i in range(n):
    for j in range(m):
        if i%2 == 0: #홀수 행 WBWB..배열로 만듬
            if j%2 == 1 and board[i][j] == 'W':
                count2[i][j] = 1
            elif j%2 == 0 and board[i][j] == 'B':
                count2[i][j] = 1
        else: #짝수 행 BWBW..배열로 만듬
            if j%2 == 1 and board[i][j] == 'B':
                count2[i][j] = 1
            elif j%2 == 0 and board[i][j] == 'W':
                count2[i][j] = 1

result = 2500

for i in range(int(n-8+1)):
    for j in range(int(m-8+1)):
        sum = 0
        for a in range(8):
            for b in range(8):
                sum += count1[i+a][j+b] #8x8 배열의 변경 갯수 세기
        if sum < result:
            result=sum        

for i in range(int(n-8+1)):
    for j in range(int(m-8+1)):
        sum = 0
        for a in range(8):
            for b in range(8):
                sum += count2[i+a][j+b] #8x8 배열의 변경 갯수 세기
        if sum < result:
            result=sum   

print(result)