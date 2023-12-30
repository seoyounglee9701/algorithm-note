# 1956: 운동
# https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-1956%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9A%B4%EB%8F%99
# pypy 통과
import sys 
input = sys.stdin.readline 

V,E=map(int, input().split(' '))
INF=sys.maxsize 
town=list(list(INF for _ in range(V+1)) for _ in range(V+1))

for _ in range(E):
    a,b,c=map(int, input().split(' '))
    town[a][b]=c 

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            town[i][j]=min(town[i][j], town[i][k]+town[k][j])

answer=INF 
for v in range(1,V+1):
    answer=min(answer, town[v][v])

if answer==INF: 
    answer = -1 

print(answer)