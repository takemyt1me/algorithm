def solution(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(M): #key의 앞 뒤에 MXN 인 사각형 붙이기
        for j in range(N):
            key[i].insert(0, 0)
            key[i].insert(len(key[i]), 0)
    
    for _ in range(N): #key의 위 아래에 NX(M+2N) 사각형 붙이기
        key.insert(0, [0]*(M+2*N))
        key.insert(len(key), [0]*(M+2*N))

    for i in range(N): #lock의 0, 1 뒤집기
        for j in range(N):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                lock[i][j] = 1
    
    arr1 = []
    count = 4
    while count: #4가지 방향의 key 경우의 수 구하기
        for i in range(M+N+1):
            for j in range(M+N+1):
                temp = [[0 for k in range(N)] for l in range(N)]
                for a in range(N):
                    for b in range(N):
                        temp[a][b] = key[i+a][j+b]
                arr1.append(temp)
        
        key.reverse()
        key = list(zip(*key))
        count -=1

    result = 0        
    for i in range(4*(M+N+1)**2):
            res = 0
            for a in range(N):
                for b in range(N):
                    if arr1[i][a][b] == lock[a][b]:
                        res +=1
            if result < res:
                result = res

    if result == M**2:
        answer = True
    else:
        answer = False

    return answer

board1=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
board2=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
boolean = solution(board1, board2)

print(boolean)