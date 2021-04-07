# https://www.acmicpc.net/problem/1697
# 풀이) BFS + DP

from collections import deque

n, k = map(int, input().split())

dp = [1e9] * 100001

t = 0

q = deque([n])
dp[n] = 0

while q:
    now = q.popleft()
    t = dp[now] + 1
    
    if now + 1 < 100001:
        if dp[now+1] > t:
            dp[now+1] = t
            q.append(now+1)

    if now-1 >= 0:
        if dp[now-1] > t:
            dp[now-1] = t
            q.append(now-1)

    if now * 2 < 100001:
        if dp[now*2] > t:
            dp[now*2] = t
            q.append(now*2)

print(dp[k])






