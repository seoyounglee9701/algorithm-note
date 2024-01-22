# 2606. 바이러스: https://www.acmicpc.net/problem/2606
# https://bio-info.tistory.com/152
from collections import deque


count=0

def DFS(v):

    global count
    visited[v]=1

    for i in graph[v]:
        if visited[i]==0:
            DFS(i)
            count+=1 
n=int(input())
v=int(input())
graph=[[]*(n+1) for _ in range(n+1)]

for i in range(v):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
DFS(1)
print(count)