# https://programmers.co.kr/learn/courses/30/lessons/72413
# 카카오 2021 공채
# 풀이) 다익스트라

import heapq

def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])

    INF = 1e9
    cost = INF
    for i in range(1, n+1):
        cost = min(cost, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))
        
    return cost 
    


def dijkstra(graph, start, dst):
    n = len(graph)
    q = []
    INF = 1e9
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된적이 있으면 무시
        if distance[now] < dist: 
            continue

        # 현재 노드와 인접한 노드들의 거리 계산
        for idx, i in enumerate(graph[now]):
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[dst]


n, s, a, b, fares = 6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# n, s, a, b, fares = 7,	3,  4,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))
