# 2098
# https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-DP-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9-lso2bk58

import sys 
N=int(input())
world=[]
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))
   
dp={}

def DFS(now, visited):
    if visited==(1<<N)-1:
        if world[now][0]:
            return world[now][0]
        else:
            return int(1e9)
        
    if(now, visited) in dp:
        return dp[(now, visited)]
    
    min_cost=int(1e9)
    for next in range(1, N):
        if world[now][next]==0 or visited & (1<<next):
            continue 
        cost = DFS(next, visited| (1<<next)) + world[now][next]
        min_cost=min(cost, min_cost)
    
    dp[(now, visited)]=min_cost 
    return min_cost 

print(DFS(0,1))