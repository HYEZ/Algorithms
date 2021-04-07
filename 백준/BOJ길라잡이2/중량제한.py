# https://www.acmicpc.net/problem/1939
# 풀이) BFS + 이진탐색

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

x, y = map(int, input().split())

def bfs(c):
    q = deque([x])
    visited = [0] * (n+1)
    visited[x] = 1 
    while q:
        v = q.popleft()
        for dest, cost in graph[v]:
            if not visited[dest] and c <= cost:
                    visited[dest] = 1 
                    q.append(dest)

    return visited[y]

start, end = 1, 1000000000
result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

