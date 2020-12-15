# https://www.acmicpc.net/problem/1715
 
#  각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 
#  이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

import heapq
n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

res = 0
while len(cards) != 1:
    a = heapq.heappop(cards) 
    b = heapq.heappop(cards)
    res += a + b
    heapq.heappush(cards, a+b)

print(res)