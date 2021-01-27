# https://www.acmicpc.net/problem/2583
# 풀이) DFS

import sys
sys.setrecursionlimit(10**7)


n, m, k = map(int, input().split())

arr = [[0] * (m) for _ in range(n)]

dx = [0 , 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    sy, sx, ey, ex = map(int, input().split()) # 직사각형 시작점, 끝점
    sx, ex = n - ex, n - sx - 1
    ey -= 1 

    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            arr[i][j] = -1

def dfs(x, y, c):
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                c = dfs(nx, ny, c+1)
    return c

cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            d = dfs(i, j, 1)
            cnt += 1
            res.append(d)


print(cnt)
print(' '.join(list(map(str, sorted(res)))))




