# https://programmers.co.kr/learn/courses/30/lessons/12913
# 풀이) DP

def solution(land):
    n, m = len(land), len(land[0])
    dp = [[0] * m for _ in range(n)] 
    dp[0] = land[0]
    for i in range(1, n):
        for j in range(m):
            dp[i][j] = land[i][j] + max(dp[i-1][0:j] + dp[i-1][j+1:m])
    
    return max(dp[-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	
print(solution(land))
