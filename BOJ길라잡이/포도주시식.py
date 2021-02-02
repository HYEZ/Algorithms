# https://www.acmicpc.net/problem/2156/
# 풀이) DP

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = arr[i] + arr[i-1]
    elif i == 2:
        dp[i] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    else:
        dp[i] = max(dp[i-1], dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

if n == 0:
    print(0)
else:
    print(dp[-1])
