# 1956.운동
# https://www.acmicpc.net/problem/1956
# https://ryu-e.tistory.com/47
# 시간 초과
import sys 
INF = int(1e9)

v, e = map(int, sys.stdin.readline().split()) # v개 마을, e개 도로 

# 2차원 그래프, 모든 값을 무한으로 초기화
graph = [[INF] *(v+1) for _ in range(v+1)] # 거리를 담는 테이블 

# a->b 마을 가는 도로 길이를 c로 넣기 
for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().split())
    graph[a][b]=c 

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

result=INF 
for i in range(1,v+1):
    result=min(result, graph[i][i])

if result==INF: 
    print(-1) 
else:
    print(result) 
