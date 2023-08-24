nums = list(map(int, input().split()))

count = 0

if nums[0] == 1:
    for i in range(7):
        if (nums[i+1]-nums[i])==1:
            count +=1

    if count == 7:
        print('ascending')
    else:
        print('mixed')

elif nums[0] == 8:
    for i in range(7):
        if(nums[i]-nums[i+1])==1:
            count+=1

    if count == 7:
        print('descending')
    else:
        print('mixed')

else:
    print('mixed')