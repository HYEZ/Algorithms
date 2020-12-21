# https://www.acmicpc.net/problem/11404

n = int(input())
m = int(input())

graph = [[1000000] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0


# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end =' ')
    
    print()