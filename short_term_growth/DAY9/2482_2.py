# 2482. 색상환
# https://www.acmicpc.net/problem/2482
# https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-2482%EB%B2%88-%EC%83%89%EC%83%81%ED%99%98-Java-Python

import sys 
input = sys.stdin.readline 
MOD=1000000003

N=int(input())
K=int(input())

dp=[[0]*(N+1) for i in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1 
    dp[i][1] = i 

for i in range(3, N+1):
    for j in range(2, int((i+1)/2)+1):
        dp[i][j]=(dp[i-1][j]+dp[i-2][j-1]) % MOD

print((dp[N-3][K-1] + dp[N-1][K]) % MOD)