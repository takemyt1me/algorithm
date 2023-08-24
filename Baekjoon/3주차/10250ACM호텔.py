case = int(input())

def room_num(H, N):
    line = 1   
    height =0
    if N//H == 0:
        num = N*100+line
    elif N%H == 0:
        line += (N//H-1)
        height += H
        num = height*100 + line
    else:
        line += N//H
        height += N%H
        num = height*100+line

    return num

for _ in range(case):
    h, w, n = map(int, input().split())
    print(room_num(h, n))