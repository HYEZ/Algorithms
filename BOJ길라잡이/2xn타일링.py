# https://www.acmicpc.net/problem/11726
# 풀이) DP

n = int(input())

dp = [0] * (n+1)


dp[1] = 1

if n >= 2:
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[-1]%10007)
