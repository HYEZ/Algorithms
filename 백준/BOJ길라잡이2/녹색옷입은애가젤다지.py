# https://www.acmicpc.net/problem/4485
# 풀이) 다익스트라
import sys
input = sys.stdin.readline
import heapq

INF = 1e9
t = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    distance = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0)) # cost, x, y
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                cost = arr[nx][ny] + dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    print(f'Problem {t}:', distance[-1][-1])
    t += 1



