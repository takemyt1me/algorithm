N = int(input())

for _ in range(N):
    cnt, words = input().split()
    for word in words:
        print(word*int(cnt), end ='')
    print()