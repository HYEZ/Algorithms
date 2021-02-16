# https://www.acmicpc.net/problem/2667
# 풀이) DFS

n = int(input())
arr = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    data = list(map(int, input()))
    arr.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                cnt = dfs(nx, ny, cnt+1)
    return cnt

res = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt = dfs(i, j, 1)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)