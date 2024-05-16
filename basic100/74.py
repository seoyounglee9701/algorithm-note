# 6074: [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)

# 영문 소문자(a~z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

c=ord(input())
t=ord('a')
while(t<=c):
    print(chr(t),end=' ')
    t+=1


# print(ord('a'))
# print(ord('A'))

# print(chr(65))
# print(chr(97))