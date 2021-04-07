# https://www.acmicpc.net/problem/1826
# 풀이) 그리디(최소힙+최대힙) 

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(arr, (a, b))

loc, p = map(int, input().split())

q = []
cnt = 0 # 주유소 거치는 횟수
while p < loc:
    while arr and arr[0][0] <= p:
        a, b = heapq.heappop(arr)
        heapq.heappush(q, (-b, a))
    
    if not q:
        cnt = -1
        break
    
    b, a = heapq.heappop(q)
    p += -b
    cnt += 1 # 주유소 한번 거침

print(cnt)

