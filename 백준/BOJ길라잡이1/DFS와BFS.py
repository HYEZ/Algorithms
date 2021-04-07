# https://www.acmicpc.net/problem/1260
# 풀이) DFS, BFS

from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    graph[i].sort()



def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    
def dfs(graph, visited, now):
    visited[now] = 1
    print(now, end=' ')
    for i in graph[now]:
        if not visited[i]:
            dfs(graph, visited, i)
    


dfs(graph, [0] * (n+1), v)
print()
bfs(graph, [0] * (n+1), v)
