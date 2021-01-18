# https://www.acmicpc.net/problem/13460
# 풀이) bfs 
# # - 다시풀기!!!!

from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = []
for _ in range(n):
    data = list(input())
    arr.append(data)

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

q = deque([(rx, ry, bx, by)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[-1]*m for _ in range(n)]for _ in range(m)] for _ in range(n)]
visit[rx][ry][bx][by] = 0

def move(x, y, dx, dy):
    cnt = 0
    while True:
        nx, ny = x+dx, y+dy
        cnt += 1
        if arr[nx][ny] == 'O':
            return (nx, ny, cnt)
        elif arr[nx][ny] == '#':
            return (x, y, cnt-1)
        x, y = nx, ny

def bfs():
    while q:
        rx, ry, bx, by = q.popleft()    

        if visit[rx][ry][bx][by] > 10:
            continue
        if arr[rx][ry] == 'O':
            return visit[rx][ry][bx][by]

        for i in range(4):
            nrx, nry, nrd = move(rx, ry, dx[i], dy[i])
            nbx, nby, nbd = move(bx, by, dx[i], dy[i])

            if arr[nbx][nby] == 'O':
                continue
            
            if nrx == nbx and nry == nby:
                if nrd > nbd:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            
            if visit[nrx][nry][nbx][nby] != -1: # 이미 방문된적이 있으면
                continue

            visit[nrx][nry][nbx][nby] = visit[rx][ry][bx][by] + 1
            q.append((nrx, nry, nbx, nby))

    return -1


print(bfs())



