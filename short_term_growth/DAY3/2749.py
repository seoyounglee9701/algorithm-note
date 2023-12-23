# 피보나치 수 3
# https://www.acmicpc.net/problem/2749
# 2749
# date: 23-12-22
# https://hseungyeon.tistory.com/m/295
n=int(input())
k=10**6
p=15*10**5

n%=p
a,b=0,1
for i in range(n-1):
    a,b=b%k, (a+b)%k 
print(b)