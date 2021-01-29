# https://www.acmicpc.net/problem/2512
# 풀이) Binary Search

n = int(input())
arr = list(map(int, input().split()))
total = int(input())

def binary_search(start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        new_arr = [x if x <= mid else mid for x in arr ]
        if sum(new_arr) <= total:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


res = binary_search(0, max(arr))
print(res)
