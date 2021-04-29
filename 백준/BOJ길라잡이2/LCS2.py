# https://www.acmicpc.net/problem/9252
# 풀이) DP

s1 = list(input())
s2 = list(input())
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
now = dp[-1][-1]
x = len(dp) - 1
y = len(dp[0]) - 1
res = []
while now != 0:
    if dp[x][y-1] == now-1 and dp[x-1][y] == now-1:
        res.append(s1[x-1])
        now -= 1 
        x -= 1
        y -= 1
    else:
        if dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -= 1



print(dp[-1][-1])
if dp[-1][-1] > 0:
    print(''.join(res[::-1]))

