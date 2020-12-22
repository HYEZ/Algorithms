# 이것이 코딩테스트다 (USACO)
# 풀이) 다익스트라

import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


start = 1
INF = 1e9
distance = [INF] * (n+1)
distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if distance[i] > cost:
            distance[i] = cost
            heapq.heappush(q, (cost, i))


max_value = max(distance[1:])
idx = distance.index(max_value)
cnt = distance.count(max_value)

print(idx, max_value, cnt)
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2