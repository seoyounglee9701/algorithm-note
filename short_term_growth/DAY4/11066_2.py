# 11066-파일합치기
# https://www.acmicpc.net/problem/11066
# 23.12.23
# https://velog.io/@seung_min/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11066%EB%B2%88-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0
# 시간 초과 

import sys 
input=sys.stdin.readline 

def solve():
    K=int(input())
    arr=[0]+list(map(int, input().split()))

    dp=[[0]*(K+1) for _ in range(K+1)]

    for i in range(1,K+1):
        for j in range(1,K+1):
            if j==i+1:
                dp[i][j]=arr[i]+arr[j] 
    

    for i in range(K-1, 0, -1):
        for j in range(1, K+1):
            if dp[i][j]==0 and j>i:
                dp[i][j]=min([dp[i][k]+dp[k+1][j] for k in range(i,j)])+sum(arr[i:j+1])

    print(dp[1][K])

T=int(input())
for _ in range(T):
    solve() 

