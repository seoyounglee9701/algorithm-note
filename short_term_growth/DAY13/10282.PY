# 10282.해킹: https://www.acmicpc.net/problem/10282
# https://studyandwrite.tistory.com/382

import sys, heapq 
input=sys.stdin.readline 
inf=int(1e9)

def dijkstra(graph, start):
    # 각 컴퓨터가 감염되기까지 걸리는 최단 시간을 기록하는 리스트
    t = [inf] * (n+1)
    t[start]=0 
    # 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
    count, endTime=0,0 
    
    pq=[] 
    heapq.heappush(pq, (0, start))
    while pq:
        curr_time, curr_computer = heapq.heappop(pq)
        if curr_time < t[curr_computer]:
            continue 
        
        for next in graph[curr_computer]:
            next_time, next_computer = next[0], next[1]
            if curr_time + next_time < t[next_computer]:
                t[next_computer]=curr_time+next_time 
                heapq.heappush(pq, (curr_time+next_time, next_computer))
    for time in t:
        if time<inf:
            count+=1
            
            if time>endTime:
                endTime=time 
    return count, endTime 

tc = int(input())

for _ in range(tc):
    # 컴퓨터 개수, 의존성 개수, 해킹당항 컴퓨터 번호
    n,d,c=map(int, input().split())
    # 의존성 그래프
    graph = [[] for _ in range(n+1)]
    
    for _ in range(d):
        # b에서 a로 향하는 간선
        a,b,s=map(int, input().split())
        graph[b].append((s,a))
    
    count, endTime=dijkstra(graph, c)
    print(count, endTime)