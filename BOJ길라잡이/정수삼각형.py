# https://www.acmicpc.net/problem/1932s
# 풀이) DP

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = arr.copy()

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(arr[i][j] + dp[i-1][j-1], arr[i][j] + dp[i-1][j])


print(max(dp[-1]))