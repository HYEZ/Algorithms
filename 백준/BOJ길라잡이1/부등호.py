# https://www.acmicpc.net/problem/2529
# 풀이) 위상정렬

from collections import deque
import copy
import heapq

k = int(input())
op = input().split()
graph = [[] for i in range(k+1)]
indegree = [0] * (k+1) # 진입 차수

for i in range(k):
    if op[i] == '<': # ->
        graph[i].append(i+1)
        indegree[i+1] += 1 

    elif op[i] == '>': # <-
        graph[i+1].append(i)
        indegree[i] += 1

def topology_sort(start, graph, indegree, flag=1):
    graph = copy.deepcopy(graph)
    indegree = copy.deepcopy(indegree)
    result = [0] * (k+1)
    q = []

    for i in range(k+1):
        if indegree[i] == 0:
            heapq.heappush(q, i * flag)

    while q:
        now = heapq.heappop(q) * flag
        result[now] = start
        start += 1

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i * flag)

    return ''.join(list(map(str, result)))

print(topology_sort(9 - k, graph, indegree, -1)) # 최대
print(topology_sort(0, graph, indegree)) # 최소
