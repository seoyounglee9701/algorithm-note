# 14002: 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002
# 24.01.03

N=int(input())
input_array=list(map(int, input().split()))

dp=[1]*N 

for i in range(N):
    for j in range(i):
        if input_array[i]>input_array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

subsequence=[]
order=max(dp)
for i in range(N-1, -1, -1):
    if dp[i]==order:
        subsequence.append(input_array[i])
        order-=1

subsequence.reverse()
print(*subsequence)