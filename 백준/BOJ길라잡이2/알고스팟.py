# https://www.acmicpc.net/problem/1261
# 풀이) 다익스트라

import sys
input = sys.stdin.readline
import heapq

INF = 1e9
m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
distance = [[INF] * m for _ in range(n)]
heapq.heappush(q, (0, 0, 0)) # cost, x, y
distance[0][0] = 0

while q:
    dist, x, y = heapq.heappop(q)
    
    # 현재 노드가 이미 처리된적이 있으면 무시
    if distance[x][y] < dist: 
        continue

    # 현재 노드와 인접한 노드들의 거리 계산
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            cost = dist + arr[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny)) 

print(distance[-1][-1])
