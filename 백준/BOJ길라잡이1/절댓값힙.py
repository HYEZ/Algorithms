# https://www.acmicpc.net/problem/11286
# 풀이) haepq

import heapq

q = []
n = int(input())
res = []
for _ in range(n):
    data = int(input())
    if data == 0:
        if len(q) == 0:
            res.append(0)
        else:
            res.append(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(data), data))
        

for i in res:
    print(i)
    

    
