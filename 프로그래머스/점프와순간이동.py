# https://programmers.co.kr/learn/courses/30/lessons/12980
# 풀이) 그리디

# 그리디
def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1

    return answer


# DP: 효율성 실패
def solution_dp(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2])

    return dp[n]


n = 6
print(solution(n))