# 2263. 트리의 순회
# https://www.acmicpc.net/problem/2263
# https://velog.io/@bae_mung/Python-BOJ-2263-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C

import sys 
sys.setrecursionlimit(10**9)
input=sys.stdin.readline 

def preorder(in_start, in_end, post_start, post_end):
    if(in_start>in_end) or (post_start>post_end):
        return 
    
    parents=postorder[post_end]
    print(parents, end=" ")

    left=position[parents]-in_start 
    right=in_end-position[parents]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)

n=int(input())
inorder=list(map(int, input().split()))
postorder=list(map(int, input().split()))

position=[0]*(n+1)
for i in range(n):
    position[inorder[i]]=i 

preorder(0,n-1,0,n-1)