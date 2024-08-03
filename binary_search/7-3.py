# 이진 탐색 소스코드 구현(반복문)

def binary_search(array, target, start, end):
    while start<=end:
        mid= (start+end)//2 
        if array[mid]==target:
            return mid 
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1 
    return None

n, target = list(map(int, input().split()))
array=list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result==None:
    print("No element")
else:
    print(result+1)