# https://www.acmicpc.net/problem/1915
# 풀이) DP

n, m = map(int, input().split())
arr = []
for _ in range(n):
    data = list(map(int, list(input())))
    arr.append(data)



for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(arr[i][j], max_value)

print(max_value**2)
