# 3197번
# 23.12.16
# 백조의 호수
# 참고링크: https://life318.tistory.com/17

import sys 
from collections import deque 
move_r = [-1, 1, 0, 0] # up down left right
move_c = [0, 0, -1, 1] 
r,c = map(int, sys.stdin.readline().split())

array=[] 
time=[[0]*c for _ in range(r)]

def oob(r, c, max_r, max_c):
    return not (r<max_r and r>=0 and c<max_c and c>=0)

def bfs(array, max_r, max_c, q):
    while q:
        t = q.popleft() 
        for i in range(4):
            new_r = t[0]+move_r[i]
            new_c = t[1]+move_c[i]
            if not oob(new_r, new_c, max_r, max_c) and array[new_r][new_c] == 'X' and not visited[new_r][new_c]:
                q.append([new_r, new_c, t[2]+1])
                time[new_r][new_c]=t[2]+1
                visited[new_r][new_c]=1
                continue 
            else:
                continue 
    return t[2] 

def bfs_binary(min_time, max_time):
    answer=0 
    while min_time <= max_time:
        mid_time=(max_time+min_time)//2
        q=deque([swan[0][0], swan[0][1]])
        visited=[[0]*c for _ in range(r)]
        flag=0
        while q:
            t=q.popleft() 
            for j in range(4):
                new_r=t[0]+move_r[j]
                new_c=t[1]+move_c[j]
                if swan[1][0] == new_r and swan[1][1] ==new_c:
                    flag=1 
                    break
                if not oob(new_r, new_c, r, c) and time[new_r][new_c] <= mid_time and not visited[new_r][new_c]:
                    q.append([new_r, new_c])
                    visited[new_r][new_c]=1
            if flag==1:
                break;
        if flag==1:
            answer = mid_time
            max_time = mid_time-1
        else:
            min_time = mid_time+1
    return answer 

# build 2D array 
for i in range(r):
    array.append(list(sys.stdin.readline().strip()))

swan=[]

q=deque() 
visited=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if array[i][j] == 'L' or array[i][j] == '.':
            if array[i][j] == 'L':
                swan.append([i, j])
            q.append([i,j,0])
            visited[i][j]=1
min_time=0
max_time=bfs(array, r,c, q)

print(bfs_binary(min_time, max_time))
                