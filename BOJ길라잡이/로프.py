# https://www.acmicpc.net/problem/2217
# 풀이) 우선순위큐(heapq)

import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

max_value = q[0] * n

while q:
    now = heapq.heappop(q)
    if len(q) == 0:
        max_vlaue = max(max_value, now)
    else:
        max_value = max(max_value, q[0] * len(q))
print(max_value)