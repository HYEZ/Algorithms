# https://www.acmicpc.net/problem/10159
# 풀이) 플로이드 워셜

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(lambda x : int(x) - 1, input().split())
    graph[a][b] = 1
    graph[b][a] = -1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1

for i in range(n):
    print(graph[i].count(INF))
