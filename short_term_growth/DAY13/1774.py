# 1774. 우주신과의 교감: https://www.acmicpc.net/problem/1774

# https://hbj0209.tistory.com/107

import sys 
input = sys.stdin.readline 

# 크루스칼 알고리즘을 위한 union-find
def find(c):
    if parent[c]==c:
        return c 
    else:
        parent[c]=find(parent[c])
    return parent[c]

def union(a,b):
    a,b=find(a), find(b)
    parent[max(a,b)]=min(a,b)

def check(a,b):
    return find(a)==find(b) 

def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

N, M = map(int, input().split()) # 우주신 개수, 이미 연결된 통로 개수
parent=[i for i in range(N)] # 루트 노드를 저장할 list

coordinate, graph=[], []
answer=0 


for _ in range(N):
    x,y=map(int, input().split()) # 우주신들의 좌표
    coordinate.append((x,y)) # 좌표값을 저장
    
# 이미 연결된 통로는 union을 통해 이어줌
for _ in range(M):
    x,y = map(int, input().split())
    union(x-1,y-1)

# 모든 좌표에 대해 길이 구해줌
for i in range(N-1):
    for j in range(i+1, N):
        graph.append((i,j, dist(coordinate[i], coordinate[j])))
        
graph.sort(key=lambda x:x[2])
for i in graph:
    if not check(i[0], i[1]):
        union(i[0], i[1])
        answer+=i[2]

print('%.2f' %(answer))