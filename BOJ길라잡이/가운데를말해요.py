# https://www.acmicpc.net/problem/1655
# 풀이) heapq (max heap, min heap)

import sys, heapq
input = sys.stdin.readline
  
n = int(input())
min_heap = []
max_heap = []
res = []
for _ in range(n):
    data = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-1 * data, data))
    else:
        heapq.heappush(min_heap, (data, data))
    
    if min_heap and min_heap[0][1] < max_heap[0][1]:
        a = heapq.heappop(min_heap)[1]
        b = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (b, b))
        heapq.heappush(max_heap, (-1 * a, a))

    res.append(max_heap[0][1])

for i in res:
    print(i)

    

