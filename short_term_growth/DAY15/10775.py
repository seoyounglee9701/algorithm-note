# 10775:공항 - https://www.acmicpc.net/problem/10775
# https://lagooni.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10775%EB%B2%88-%EA%B3%B5%ED%95%AD
# 시간초과
import sys 

g=int(sys.stdin.readline().rstrip())
p=int(sys.stdin.readline().rstrip())

count=0 

gate_list=[0 for _ in range(g)]
plane_list=[] 

for i in range(p):
    plane_list.append(int(sys.stdin.readline().rstrip()))

for i in plane_list:
    p_idx=i-1
    if sum(gate_list)==len(gate_list):
        break 

    if gate_list[p_idx]==0:
        gate_list[p_idx]=1 
    else:
        for j in range(p_idx, -1, -1):
            if gate_list[j]==0:
                gate_list[j]==1 
                break 
            break 
print(sum(gate_list))


