# 17420: 깊콘이 넘쳐 흘러 - https://www.acmicpc.net/problem/17420
# https://velog.io/@chang626/17420-%EA%B9%8A%EC%BD%98%EC%9D%B4-%EB%84%98%EC%B3%90%ED%9D%98%EB%9F%AC

import sys 
import math 
read = sys.stdin.readline 

n=int(read())
A=list(map(int, read().split()))
B=list(map(int, read().split()))

arr = [] 

for r1, r2 in zip(A,B):
    arr.append([r1,r2])

arr.sort(key=lambda x: (x[1], x[0]))

previous=arr[0][1]
cur_max=-1 
answer=0
cnt=0

for i in range(n):
    if previous > arr[i][0]:
        previous = max(previous, arr[i][1])
        cnt= math.ceil((previous-arr[i][0])/30)
        arr[i][0] += cnt * 30 
        answer += cnt 

    cur_max = max(cur_max, arr[i][0])

    if i+1<n and (arr[i][1]!=arr[i+1][1]):
        previous=cur_max 

print(answer)
