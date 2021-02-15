# https://www.acmicpc.net/problem/13305
# 풀이) 그리디


n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1e9
total = 0
for i in range(n-1):
    min_price = min(price[i], min_price) 
    total += min_price * dist[i]
    
print(total)