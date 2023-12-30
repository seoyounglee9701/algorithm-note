# 운동
# https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-1956%EB%B2%88-%EC%9A%B4%EB%8F%99-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys 
input = sys.stdin.readline 
MAX=sys.maxsize 
V,E=map(int, input().split())
arr=[[MAX for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    arr[a][b]=cost 

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j]=arr[i][k]+arr[k][j] 

result=MAX 
for i in range(1,V+1):
    result=min(result, arr[i][i])

if result==MAX:
    print('-1')
else:
    print(result)