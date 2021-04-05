# https://www.acmicpc.net/problem/2585
# 풀이) BFS + Binary Search

import math
from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]


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
    return False
        
start = 0
end = 10000
result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid * 10):
        result = mid
        end = mid - 1
    else:
        start = mid + 1


print(result)

