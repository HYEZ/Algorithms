# https://programmers.co.kr/learn/courses/30/lessons/12900
# 풀이) DP

def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007 # 매번 나눠줘야 시간초과 안남
    
    return dp[-1]




n = 60000
print(solution(n))
