# 6807-레이저통신
# https://www.acmicpc.net/problem/6087
# 23.12.23
# https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-6087%EB%B2%88-%EB%A0%88%EC%9D%B4%EC%A0%80-%ED%86%B5%EC%8B%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 시간초과, 메모리 초과
from collections import deque 
import sys 
input = sys.stdin.readline 
MAX= sys.maxsize 

M, N = map(int, input().split())
arr=[]
C=[] 

for i in range(N):
    arr.append(list(input().strip()))
    for j in range(M):
        if arr[i][j] =='C':
            C.append((i, j))
start, end=C[0], C[1] 

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(a,b):
    global answer 
    q=deque() 
    q.append((a,b,-1,0))
    visited=[[0]*M for _ in range(N)]
    visited[a][b]=0 
    while q:
        x,y,dir, result=q.popleft() 
        # 도착 지점이라면 최소값 계산후 continue
        if(x,y)==end:
            answer=min(answer, result)
            continue 
        for ndir in range(4):
            nx=x+dx[ndir]
            ny=y+dy[ndir]

            if 0<=nx<N and 0<=ny <M and arr[nx][ny] !="*":
                # 현재까지 사용한 거울의 수가 현 위치 최솟값과 같다면
                if result==visited[x][y]:
                    #처음 방문한다면
                    if not visited[nx][ny]:
                        if dir==-1 or dir==ndir:
                            visited[nx][ny]=result 
                            q.append((nx,ny,ndir,result))
                        elif dir !=ndir:
                            visited[nx][ny]=result+1
                            q.append((nx,ny,ndir,result+1))
                    # 이미 방문했다면
                    else:
                        if dir==ndir and visited[nx][ny]>=result:
                            visited[nx][ny]=result
                            q.append((nx,ny,ndir,result))
                        elif dir != ndir and visited[nx][ny]>=result+1:
                            visited[nx][ny]=result+1
                            q.append((nx,ny,ndir,result+1))
