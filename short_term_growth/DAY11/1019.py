# 1019. 책 페이지
# https://www.acmicpc.net/problem/1019
# https://it-garden.tistory.com/262

import sys 
n=int(sys.stdin.readline().strip())
a=[0]*10
b=1
while n!=0:
    while n % 10 !=9:
        for i in str(n):
            a[int(i)] += b
        n -=1
    if n<10:
        for k in range(n+1):
            a[k] += b 
        a[0] -= b 
        break 
    else:
        for i in range(10):
            a[i]+=(n//10+1)*b 
    a[0]-=b 
    b*=10 
    n//=10 
for i in a: 
    print(i,end=' ')
            