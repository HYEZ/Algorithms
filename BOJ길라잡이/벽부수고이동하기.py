# https://www.acmicpc.net/problem/2206
# 풀이) 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
arr = []
distance = [[INF] * m for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().replace('\n', '')))
    arr.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    distance[0][0] = 1

    while q:
        t, x, y = heapq.heappop(q)

        # 현재 노드와 인접한 노드들의 거리 계산
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                cost = distance[x][y] + 1
                
                if cost < distance[nx][ny]:
                    if t == 1:
                        if arr[nx][ny] == 0:
                            distance[nx][ny] = distance[x][y] + 1
                            heapq.heappush(q, (t, nx, ny))
                    else:
                        distance[nx][ny] = distance[x][y] + 1
                        heapq.heappush(q, (arr[nx][ny], nx, ny))

dijkstra()

if distance[n-1][m-1] == INF:
    print(-1) 
else:
    print(distance[n-1][m-1])
