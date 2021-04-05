# https://www.acmicpc.net/problem/2585
# 풀이) 최단거리

import math, heapq
from collections import deque
n, k = map(int, input().split())
arr = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

s = (0, 0)
t = (10000, 10000)

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def bfs(c):
    visited = [0] * (n+1)
    q = deque([0])
    cnt = 0

    while q:
        if cnt > k:
            return False
        
        for _ in range(len(q)):
            vertex = q.popleft()
            if not visited[vertex]:
                visited[vertex] = 1

                for i in range(1, n+1):
                    dist = distance(arr[vertex], arr[i])
                    if dist <= c:
                        dist_dest = distance(t, arr[i])
                        if dist_dest <= c:
                            return True
                        q.append(i)
        cnt += 1
        
start = 0
end = 10000
while start <= end:
    mid = (start + end) // 2
    if bfs(mid * 10):
        result = mid
        end = mid - 1
    else:
        start = mid + 1


print(result)

