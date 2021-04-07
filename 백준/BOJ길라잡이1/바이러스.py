# https://www.acmicpc.net/problem/2606
# 풀이) DFS

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

dfs(1)
print(sum(visited) - 1)
