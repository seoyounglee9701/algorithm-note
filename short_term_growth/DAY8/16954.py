# 16954: 움직이는 미로 탈출 
# https://www.acmicpc.net/problem/16954
# https://data-flower.tistory.com/92

import sys 
input = sys.stdin.readline 
from collections import deque 

# 맵 리스트, 벽 위치 집합, 정답 변수 생성
board, wall, answer = [input().rstrip() for _ in range(8)], set(), 0 
# 벽 위치 추가 
for i in range(8):
    for j in range(8):
        if board[i][j]=='#':
            wall.add((i, j)) 

# 9가지 방향 정의
steps=[[0,0],[-1,0], [1,0],[0,-1], [0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

# 방문 표시 집합 생성
visited=set() 
# 큐 정의 
q= deque() 
q.append((7,0))

# 큐가 빌 때까지 반복
while q:
    for _ in range(len(q)):
        x,y=q.popleft() 
        # 현재 위치에 벽이 있다면 건너 뛰기
        if(x,y) in wall:
            continue 
        # 현재 위치가 도착 지점이라면 
        if x==0 and y==7: 
            answer=1
            break 
        for dx, dy in steps:
            nx = x+dx 
            ny = y+dy 
            # 조건을 만족한다면
            if 0<=nx <=7 and 0<=ny<=7 and not (nx, ny) in visited and not (nx, ny) in wall:
                visited.add((nx,ny))
                q.append((nx,ny))
    if wall:
        visited=set() 
    next_wall=set() 
    for x,y in wall:
        if x<7: 
            next_wall.add((x+1,y))
    wall = next_wall 

print(answer) 