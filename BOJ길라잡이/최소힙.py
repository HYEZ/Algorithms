# https://www.acmicpc.net/problem/1927
# 풀이) heapq

import heapq

n = int(input())
q = []
res = []

for _ in range(n):
    o = int(input())
    if o == 0:
        if len(q) == 0:
            res.append(0)
        else:
            res.append(heapq.heappop(q))
    else:
        heapq.heappush(q, o)
for i in res:
    print(i)

        