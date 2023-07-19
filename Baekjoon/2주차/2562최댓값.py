arr = []
for _ in range(9):
    arr.append(int(input()))

arr_sorted = sorted(arr)
count = 0
for i in range(9):
    if arr[i] == arr_sorted[8]:
        count = i+1

print(f'{arr_sorted[8]}\n{count}')