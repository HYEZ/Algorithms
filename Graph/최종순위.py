# https://www.acmicpc.net/problem/3665

# 풀이) 위상정렬

from collections import deque
import sys
input = sys.stdin.readline


case = int(input())
answer = []
for c in range(case):
    n = int(input()) # 팀의 수
    t = list(map(int, input().split())) # 작년 등수
    m = int(input()) # 상대적인 등수가 바뀐 쌍의 수 m

    indegree = [0] * (n + 1) # 진입차수
    graph = [[False] * (n+1) for i in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[t[i]][t[j]] = True 
            indegree[t[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split()) # a팀, b팀의 순서가 바뀐거!

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1


       
    result = []
    certain = True
    cycle = False
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)


    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()
