# https://www.acmicpc.net/problem/1149
# 풀이) DP
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

dp = [[-1]*3 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))