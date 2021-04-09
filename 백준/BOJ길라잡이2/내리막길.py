# https://www.acmicpc.net/problem/1520
# 풀이) DFS + DP

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1: # 도착지점 방문 시
        return True
    
    if dp[x][y] != -1: # 방문 처리
        return dp[x][y] 

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue

        if arr[nx][ny] < arr[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
