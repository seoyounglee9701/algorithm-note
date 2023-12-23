# 23971.py
# ZOAC 4
# https://www.acmicpc.net/problem/23971
# 23.12.22
# 출처 :https://velog.io/@qwerty1434/%EB%B0%B1%EC%A4%80-23971%EB%B2%88-ZOAC-4
H, W, N, M = list(map(int, input().split(' ')))

import math 

a=math.ceil(H/(N+1))
b=math.ceil(W/(M+1))
answer=a*b 
print(answer)