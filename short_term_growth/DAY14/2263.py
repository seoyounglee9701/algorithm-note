# 2263. 트리의 순회
# https://www.acmicpc.net/problem/2263
# https://ku-hug.tistory.com/135
# 런타임 에러
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd]
    
    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]
    
    print(root, end = " ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)