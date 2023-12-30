# 10217: KCM Travel - https://www.acmicpc.net/problem/10217
# 23.12.29
# https://velog.io/@yeomja99/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10217%EB%B2%88-KCM-Travel
# 시간초과

import sys
from collections import deque

def dijkstra():
    q = deque([(1, 0, 0)])
    dist_cost = [[1e10 for t in range(m+1)]for x in range(n+1)]
    dist_cost[1][0] = 0 # 시작노드 1의 cost(0)의 dist 업데이트
    while q:
        node, cost, dist = q.popleft()
        if dist_cost[node][cost] < dist:
            continue
        for nnode, ncost, ndist in graph[node]:
            temp_cost = cost + ncost
            temp_dist = dist_cost[node][cost] + ndist
            if temp_cost <= m and dist_cost[nnode][temp_cost] > temp_dist:
                q.append((nnode, temp_cost, temp_dist))
                for i in range(temp_cost, m+1):
                    if dist_cost[nnode][i] > temp_dist:
                        dist_cost[nnode][i]=temp_dist
                    else: break
    if dist_cost[n][m] == 1e10:
        print("Poor KCM")
        return
    print(dist_cost[n][m])


t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[]for i in range(n+1)]
    for i in range(k):
        # u: 출발 공항, v: 도착 공항, c: 비용, d: 소요시간
        u, v, c, d = map(int, sys.stdin.readline().split())
        graph[u].append([v, c, d])

    dijkstra()