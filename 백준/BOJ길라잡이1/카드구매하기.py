# https://www.acmicpc.net/problem/11052
# 풀이) DP

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = arr[1]

for i in range(2, n + 1):
    max_vlaue = arr[i]
    for j in range(i//2, i):
        if dp[j] + dp[i-j] > max_vlaue:
            max_vlaue = dp[j] + dp[i-j]
    dp[i] = max_vlaue
    
print(dp[-1])
