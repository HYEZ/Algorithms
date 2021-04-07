# https://www.acmicpc.net/problem/10815
# 풀이) Binary Search

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)

    return right_idx - left_idx
    

n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    d = count_by_range(arr1, x, x)
    print(d, end=' ')

