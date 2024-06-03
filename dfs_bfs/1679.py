# 1679. 숨바꼭질: https://www.acmicpc.net/problem/1697
# https://chancoding.tistory.com/193

import sys
from collections import deque 

def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if v==k:
            return arr[v]
        for n_v in (v-1, v+1, 2*v):
            if 0<=n_v<MAX and not arr[n_v]:
                arr[n_v] = arr[v]+1
                q.append(n_v)

MAX=100001
n, k = map(int, sys.stdin.readline().split())
arr=[0]*MAX 
print(bfs(n))

