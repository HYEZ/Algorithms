# https://www.acmicpc.net/problem/2579
# 풀이) DP

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(n+1)]

dp[1] = arr[1]
 
for i in range(2, n+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[-1])
