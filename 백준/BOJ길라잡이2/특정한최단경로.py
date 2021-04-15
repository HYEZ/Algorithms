# https://www.acmicpc.net/problem/1504
# 풀이) 다익스트라

import sys
input = sys.stdin.readline

import heapq

def dijkstra(start, end):
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
    
    return distance[end]

INF = int(1e9)
n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


a, b = map(int, input().split()) # 여기 반드시 지나야함

res1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, n)
res2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, n)
res = min(res1, res2)
if res >= INF:
    print(-1)
else:
    print(res)