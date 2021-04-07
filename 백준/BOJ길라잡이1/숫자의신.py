# https://www.acmicpc.net/problem/1422
# 풀이) 그리디, 정렬

from functools import cmp_to_key

arr = []
k, n = map(int, input().split())
for _ in range(k):
    arr.append(int(input()))

max_num = max(arr)
for i in range(n - k):
    arr.append(max_num)

arr = sorted(arr, key=cmp_to_key(lambda a, b: -1 if int(str(a) + str(b)) > int(str(b) + str(a)) else 1))
print(*arr, sep='')