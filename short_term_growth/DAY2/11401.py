# 11401번
# 이항계수2
# https://www.acmicpc.net/problem/11401
# https://my-coding-notes.tistory.com/94
n, k = map(int, input().split())
P=1000000007

def factorial(num, mod):
    result=1
    for i in range(2, num+1):
        result = result * i % P 
    return result 

def power(num, p, mod):
    if p==1:
        return num % mod 
    
    if p%2:
        return ((power(num,p//2,mod)**2)*num)%mod
    else:
        return(power(num, p//2, mod)**2)%mod 

print(factorial(n,P)*power((factorial(k, P) * factorial(n-k, P)), P-2, P) % P)