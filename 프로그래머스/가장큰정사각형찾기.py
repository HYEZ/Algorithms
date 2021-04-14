# https://programmers.co.kr/learn/courses/30/lessons/12905
# 풀이) DP

# 가장 큰 정사각형 찾기 
def solution(arr):
    n, m = len(arr), len(arr[0])
    dp = arr
    
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == 0:
                continue
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

    max_value = max([max(x) for x in dp])

    return max_value**2
        
  

board = [[0,0,1,1],[1,1,1,1]]	
print(solution(board))