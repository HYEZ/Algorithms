# https://www.acmicpc.net/problem/1613
# 풀이) 플로이드 워셜

import sys
input = sys.stdin.readline

INF = int(1e9)
n, k = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1


for _ in range(int(input())):
    a, b = map(int, input().split())
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])
