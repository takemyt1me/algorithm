arr = []

for _ in range(10):
    num = int(input())
    res = num%42
    arr.append(res)

result = list(set(arr))

print(len(result))