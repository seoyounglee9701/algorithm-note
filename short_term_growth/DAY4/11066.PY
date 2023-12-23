# 11066-파일 합치기
# https://www.acmicpc.net/problem/11066
# 23.12.23
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11066-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0-%EA%B3%A8%EB%93%9C3-DP
# 시간초과
import sys 
input=sys.stdin.readline 

for _ in range(int(input())):
    K=int(input())
    files=[*map(int, input().split())]
    minCost=[[0]*K for _ in range(K)] # 메모이제이션 리스트

    subSum = {-1:0} 
    for idx in range(K):
        subSum[idx]=subSum[idx-1]+files[idx] 
    
    for size in range(1,K):
        for start in range(K-1):
            end = start+size 

            if end>=len(files):
                break 

            result=float("inf")
            for cut in range(start, end):
                result = min(result, minCost[start][cut]+minCost[cut+1][end]+subSum[end]-subSum[start-1])
            minCost[start][end]=result 
    print(minCost[0][-1])
