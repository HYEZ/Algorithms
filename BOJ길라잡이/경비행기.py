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
        if cnt > k: # 연료 c를 위해 k보다 많이 방문했으면 return False
            return False
        
        for _ in range(len(q)): # q 개수만큼 방문 체크
            vertex = q.popleft()
            if not visited[vertex]:
                visited[vertex] = 1

                for i in range(1, n+1): # arr 개수만큼 체크
                    dist = distance(arr[vertex], arr[i]) # 현재 pop한 애랑 나머지 애들의 distance
                    if dist <= c: # distacne가  c보다 작으면 append
                        dist_dest = distance(t, arr[i])  
                        if dist_dest <= c: 
                            return True # 목적지까지 distance가 c보다 작으면 그냥 return
                        q.append(i)
        cnt += 1 # 방문개수 증가
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

