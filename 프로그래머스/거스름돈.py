# https://programmers.co.kr/learn/courses/30/lessons/12907
# 풀이) DP

def solution(n, money):
    dp = [1] + [0] * n
    
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price-coin]

    return dp[n] % 1000000007
    

n, money = 5, [1,2,5]	
print(solution(n, money))