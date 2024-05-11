# 15681. 트리와 쿼리 : https://www.acmicpc.net/problem/15681
# https://velog.io/@zjvlzld/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-15681

import sys 
sys.setrecursionlimit(1000000000)
N,R,Q=map(int,sys.stdin.readline().split(' ')) # 정점의 수, 루트 번호, 쿼리의 수

graph=[[] for _ in range(N+1)] # 그래프 형태로 노드를 입력 받음
visit=[-1 for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split(' '))
    graph[a].append(b) 
    graph[b].append(a) 

def dfs(now):
    global visit 
    visit[now]=1 # 나 자신을 추가해줌
    for i in graph[now]:
        if visit[i]==-1:    # 방문하지 않은 방문 가능 노드가 있다면
            visit[now]+=dfs(i) # 방문하며 그 노드 서브트리 개수를 더해줌
    return visit[now] # 내 서브트리 개수를 리턴함
dfs(R)

for _ in range(Q):
    get=int(sys.stdin.readline())
    print(visit[get])