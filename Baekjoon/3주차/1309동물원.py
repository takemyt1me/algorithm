N = int(input())

memo = [0]*100001

def f(n):
    if memo[n]!=0:
        return memo[n]
    
    elif n==1:
        memo[n] = 3
        return 3
    
    elif n==2:
        memo[n] = 7
        return 7
    
    else:
        tmp = 2*f(n-1)+f(n-2)
        memo[n] = tmp
        return tmp
    
res = f(N)%9901
print(res)  
        
    

            