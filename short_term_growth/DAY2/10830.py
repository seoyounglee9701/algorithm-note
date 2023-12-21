# 10830번
# https://www.acmicpc.net/problem/10830
# 행렬 제곱
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

import sys 
input = sys.stdin.readline 

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0 
            for i in range(n):
                e+=U[row][i] * V[i][col]
            Z[row][col] = e % 1000 
    return Z 

def square(A, B):
    if B==1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A 
    
    tmp = square(A, B//2)
    if B%2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
result = square(A, B)
for r in result:
    print(*r)


    