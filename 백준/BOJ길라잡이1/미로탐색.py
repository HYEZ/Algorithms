# https://www.acmicpc.net/problem/2178
# 풀이) DP, BFS 

from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    data = list(map(int, input()))
    arr.append(data)

INF = int(1e9)
dp = [[INF] * m for _ in range(n)]
dp[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([(0, 0)])

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
            
        cnt = dp[x][y] + arr[nx][ny] 
        if arr[nx][ny] == 1 and  cnt < dp[nx][ny]:
            dp[nx][ny] = cnt
            q.append((nx, ny))
    

print(dp[n-1][m-1])

