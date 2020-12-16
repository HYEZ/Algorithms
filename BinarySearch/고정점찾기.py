# 이것이 코딩테스트다 (아마존 인터뷰)

# 고정점 = 수열의 원소 중에서 그 값이 인덱스와 동일한 원소

n = int(input())
arr = list(map(int, input().split()))

def binary_search(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search(arr)) 