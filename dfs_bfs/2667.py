# 2667. 단자번호 붙이기: https://hongcoding.tistory.com/71
from collections import deque 

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(graph,a,b):
    n=len(graph)
    queue=deque() 
    queue.append((a,b))
    graph[a][b]=0 # 첫번째 집 방문처리
    count=1 

    while queue:
        x,y=queue.popleft() 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue 
            if graph[nx][ny]==1: # 방문을 안한 경우
                graph[nx][ny]=0  # 방문했던 곳은 0으로 만들기
                queue.append((nx,ny))
                count+=1 
    return count 

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph, i, j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])