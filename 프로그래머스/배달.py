# https://programmers.co.kr/learn/courses/30/lessons/12978
# 풀이) 다익스트라

import heapq
def solution(n, road, k):
    graph = [[] for _ in range(n+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    INF = int(1e9)
    q = []
    start = 1
    heapq.heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    res = 0
    for i in range(1, n+1):
        if distance[i] <= k:
            res += 1

    return res

        

    


n = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	
k = 3
print(solution(n, road, k))