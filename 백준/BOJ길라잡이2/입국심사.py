# https://www.acmicpc.net/problem/3079
# 풀이) 이진탐색

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))


start = 0
end =  max(arr) * m
while start <= end:
    mid = (start + end) // 2
    if sum([mid // x for x in arr]) >= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)
