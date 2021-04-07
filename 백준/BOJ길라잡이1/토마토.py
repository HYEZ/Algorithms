# https://www.acmicpc.net/problem/7576
# 풀이) BFS

from collections import deque

m, n = map(int, input().split())
arr = []
for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

tomato = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomato.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr, tomato):
    cnt = 0
    q = deque(tomato)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx  = x + dx[i]
            ny  = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))        

def get_day(arr):
    max_value = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
            max_value = max(arr[i][j], max_value)

    return max_value - 1

bfs(arr, tomato)
print(get_day(arr))



