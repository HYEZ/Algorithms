# https://www.acmicpc.net/problem/1202    
# 풀이) 
import heapq

jew = []
bags = []

n, k = map(int, input().split())
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jew, (m, v))

for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

answer = 0
temp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        # 가방에 넣을 수 있는 애들의 가격을 모두 우선순위 큐에 넣음
        heapq.heappush(temp_jew, -heapq.heappop(jew)[1])
    if temp_jew:
        answer -= heapq.heappop(temp_jew) # 높은 가격부터 가져오도록
    elif not jew:
        break
print(answer)