# https://www.acmicpc.net/problem/14501

n = int(input())
t, p = [], []

for i in range(n):
    data = list(map(int, input().split()))
    t.append(data[0])
    p.append(data[1]) # 저장을 다르게해야함

dp = [0 for _ in range(n)] # 돈의 최대값을 계속해서 저장하는 dp 테이블
for i in range(n): # 날짜만큼 루프
    idx = i + t[i] - 1 # dp 인덱스
    if idx < n:
        k = dp[idx-t[i]]
        if len(dp[:idx-t[i]+1]):
            k = (max(dp[:idx-t[i]+1]))
        dp[idx] = max(p[i]+k, dp[idx]) #dp[idx-t[i]]

print(max(dp))