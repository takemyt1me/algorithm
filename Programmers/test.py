def solution(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(M): #key의 앞 뒤에 MXM 인 사각형 붙이기
        for j in range(M):
            key[i].insert(0, 0)
            key[i].insert(len(key[i]), 0)
    
    for _ in range(M): #key의 위 아래에 MX3M 사각형 붙이기
        key.insert(0, [0]*(3*M))
        key.insert(len(key), [0]*(3*M))

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                lock[i][j] = 1
    
    arr1 = []
    arr2 = []
    count = 4
    while count: #4가지 방향의 key 경우의 수 구하기
        for i in range(2*M+1):
            for j in range(2*M+1):
                temp = [[0 for k in range(M)] for l in range(M)]
                for a in range(M):
                    for b in range(M):
                        temp[a][b] = key[i+a][j+b]
                arr1.append(temp)
        
        key.reverse()
        key = list(zip(*key))
        count -=1

    for i in range(N-M+1): #lock의 경우의 수 저장
        for j in range(N-M+1):
            temp = [[0 for k in range(M)] for l in range(M)]
            for a in range(M):
                for b in range(M):
                    temp[a][b]=lock[i+a][j+b]
            arr2.append(temp)
    
    result = 0        
    for i in range(4*(2*M+1)**2):
        for j in range((N-M+1)**2):
            res = 0
            for a in range(M):
                for b in range(M):
                    if arr1[i][a][b] == arr2[j][a][b]:
                        res +=1
            if result < res:
                result = res
    print(result)


board1=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
board2=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
boolean = solution(board1, board2)
