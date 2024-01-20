# 1781.컵라면 : https://www.acmicpc.net/problem/1781

import sys 
import heapq 
input=sys.stdin.readline 

N=int(input())
problem_list=[] 

for _ in range(N):
    deadline, cup_ramen = map(int, input().split())
    problem_list.append([deadline,cup_ramen])

problem_list.sort(key=lambda x:x[0])

cup_ramen_heap=[] 

for problem in problem_list:
    heapq.heappush(cup_ramen_heap, problem[1])
    if len(cup_ramen_heap)>problem[0]:
        heapq.heappop(cup_ramen_heap)
    
print(sum(cup_ramen_heap))
