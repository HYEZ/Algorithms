# https://www.acmicpc.net/problem/11657
# 풀이) 벨만포드 알고리즘


import sys
input = sys.stdin.readline

INF = float('inf') # 이게 중요함...!!!!!!!!

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


for _ in range(n-1): # n-1 번!
    for i in range(1, n+1): # n번!
        for j, cost in graph[i]:
            if distance[j] > distance[i] + cost:
                distance[j] = distance[i] + cost


# 1번 노드에서 음수 사이클이 있는지 판단
cycle = False
for i in range(1, n+1):
    for j, cost in graph[i]:
        if distance[j] > distance[i] + cost:
            cycle = True
            
if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i] if distance[i] < INF else -1)

