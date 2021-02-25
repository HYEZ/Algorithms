# https://www.acmicpc.net/problem/7569
# 풀이) BFS

from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tmp = []
arr = []
for i in range(n*h):
    data = list(map(int, input().split()))
    tmp.append(data)
    if (i+1) % n == 0:
        arr.append(tmp)
        tmp = []

tomato = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                tomato.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def bfs(arr, tomato):
    cnt = 0
    q = deque(tomato)
    while q:
        z, x, y = q.popleft()
        for i in range(6):      
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and nz >= 0 and nz < h:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    q.append((nz, nx, ny))        


def get_day(arr):
    max_value = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    return -1
                max_value = max(arr[i][j][k], max_value)

    return max_value - 1
print(arr)
bfs(arr, tomato)
print(get_day(arr))

