# https://www.acmicpc.net/problem/11047
# 풀이) 그리디

n, k = map(int, input().split())
price = []

for _ in range(n):
    data = int(input())
    if data <= k:
        price.append(data)
        
n = len(price)
res = 0
for i in range(n-1, -1, -1):
    now = price[i]
    res += k // now # 동전 사용 개수
    k = k % now # 남은 동전 수
 
print(res)
