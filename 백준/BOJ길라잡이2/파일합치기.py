# https://www.acmicpc.net/problem/11066
# 풀이) DP - 다시풀기!!!

import sys
input = sys.stdin.readline

INF = int(1e9)
t = int(input())

for _ in range(t):    
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * n for _ in range(n)]


    for k in range(1, n): # k = 1, 2, 3 when n = 4
        for i in range(n - k): # i = 0, 1, 2, 3 when k = 1 
            x, y = i, i + k
            dp[x][y] = INF
            for j in range(k):
                tmp = dp[x+1+j][y] + dp[x][y-k+j]
                dp[x][y] = min(dp[x][y], tmp)
            
            dp[x][y] += sum(arr[x:y+1])

    print(dp[0][-1])
    



