# 11049: 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049
# https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-11049-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-DP
# 23.12.23

N=int(input())
matrix=[] 
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp=[[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(0, N-i):
        if i==1:
            dp[j][j+i]=matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue 

        dp[j][j+i]=2**32 
        for k in range(j, j+i):
            dp[j][j+i]=min(dp[j][j+i],
                           dp[j][k]+dp[k+1][j+i]+matrix[j][0]*matrix[k][1]*matrix[j+i][1])
            

print(dp[0][N-1])