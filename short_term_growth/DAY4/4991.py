# 4991:로봇청소기
# https://www.acmicpc.net/problem/4991
# 23.12.23 
# https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-4991-%EB%A1%9C%EB%B4%87-%EC%B2%AD%EC%86%8C%EA%B8%B0-Python

import sys 
from collections import deque 

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def move_to_target(now_pos, target_pos):
    global w, h, board 

    que = deque() 
    is_visited=[[False for _ in range(w)] for _ in range(h)]

    x,y=now_pos 
    que.append([x,y,0])
    is_visited[x][y]=True 

    while que:
        now_x, now_y, now_cnt = que.popleft() 

        if now_x==target_pos[0] and now_y == target_pos[1]:
            return now_cnt 
        
        for t in range(4):
            nx= now_x+dx[t] 
            ny= now_y+dy[t] 

            if nx<0 or ny<0 or nx>=h or ny>=w or board[nx][ny]=='x':
                continue 
            if is_visited[nx][ny]:
                continue 

            que.append([nx,ny,now_cnt+1])
            is_visited[nx][ny]=True 
    
    return int(1e9)

def make_combination(depth, target_cnt, comb, start_pos, now_dist):
    global result, check_, targets_ 

    if now_dist>=result:
        return 
    
    if depth==target_cnt:
        if now_dist<result:
            result=now_dist 
        return 
    
    for i in range(target_cnt):
        if not check_[i]:
            n_dist=now_dist+dist[start_pos][i]

            comb.append(i)
            check_[i] = True 

            make_combination(depth+1, target_cnt, comb, i, n_dist)

            comb.pop() 
            check_[i]=False 

result=int(1e9)
while True:
    result=int(1e9)
    w,h=map(int, sys.stdin.readline().rstrip().split())
    if w==0 and h==0:
        break 
    board=[list(sys.stdin.readline().rstrip()) for _ in range(h)]

    # 먼지 칸, 출발 칸 위치 저장
    targets_=[] 
    start_pos_ = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                targets_.append([i,j])
            elif board[i][j]=='o':
                start_pos_=[i,j]
    
    dist=[[int(1e9) for _ in range(len(targets_)+1)] for _ in range(len(targets_)+1)]

    for i in range(len(targets_)):
        for j in range(len(targets_)):
            cnt=move_to_target(targets_[i], targets_[j])
            dist[i][j]=cnt
    
    for i in range(len(targets_)):
        cnt=move_to_target(start_pos_, targets_[i])
        dist[len(targets_)][i]=cnt
        dist[i][len(targets_)]=cnt
    dist[len(targets_)][len(targets_)]=0

    check_=[False for _ in range(len(targets_))]
    combs_=[] 
    make_combination(0,len(targets_), combs_, len(targets_), 0)

    if result!=int(1e9):
        print(result)
    else:
        print(-1)
        

