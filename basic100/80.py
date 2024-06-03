# 6080 : [기초-종합] 주사위 2개 던지기(설명)(py)

n, m = input().split(' ')
n=int(n)
m=int(m)

for i in range(n):
    for j in range(m):
        print(f"{i+1} {j+1}")