# https://www.acmicpc.net/problem/1238
# 풀이) 다익스트라

import sys
input = sys.stdin.readline

import heapq
INF = 1e9

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, dest):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된적이 있으면 무시
        if distance[now] < dist: 
            continue

        # 현재 노드와 인접한 노드들의 거리 계산
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[dest]

res = 0
for i in range(1, n+1):
    res = max(res, dijkstra(i, x) + dijkstra(x, i))

print(res)





