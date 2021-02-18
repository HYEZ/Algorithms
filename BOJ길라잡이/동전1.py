# https://www.acmicpc.net/problem/2293
# 풀이) DP
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
price = []

for _ in range(n):
    data = int(input())
    if data <= k:
        price.append(data)

n = len(price)
if n == 0:
    print(0)
else:
    dp = [0] * (k+1)
    for i in price:
        dp[i] += 1 # 자기 자신만으로 만드는 방법
        for j in range(i, k+1): 
            dp[j] += dp[j-i]

print(dp[-1])

