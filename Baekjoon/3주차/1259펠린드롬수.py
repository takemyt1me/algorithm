while True:
    word = input()
    if word == '0':
        break

    rvs = list(reversed(word))

    is_palindrome = True
    
    for i in range(len(word)):
        if word[i] != rvs[i]:
            is_palindrome = False

    if is_palindrome:
        print('yes')
    else:
        print('no')


