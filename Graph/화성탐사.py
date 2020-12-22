# 이것이 코딩테스트다 (ACM-ICPC)

# 출발지점 => 도착지점까지 이동할때 항상 최적의 경로를 찾도록 개발 (다익스트라)

import heapq

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = (0, 0)
INF = 1e9
distance = [[INF]*n for _ in range(n)]
distance[0][0] = graph[0][0]

q = []
heapq.heappush(q, (graph[0][0], start))

while q:
    dist, now = heapq.heappop(q)

    if distance[now[0]][now[1]] < dist:
        continue
    
    for k in range(4):
        i = now[0] + dx[k]
        j = now[1] + dy[k]
        if i < 0 or j < 0 or i >= n or j >= n:
            continue
        
        cost = dist + graph[i][j]
        if cost < distance[i][j]:
            distance[i][j] = cost
            heapq.heappush(q, (cost, (i, j)))

print(distance[n-1][n-1])








# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4