# https://www.acmicpc.net/problem/1657
# 풀이) DP

# 준이는 전체 두부가격의 합을 최대가 되게 두부를 자르려고 한다. 
# 2x1짜리 두부로 잘라내고 남은 한 칸짜리 두부는 가격이 0이기 때문에 버린다. 
# 홍준이를 도와 가격이 최대가 되게 두부판을 자르는 프로그램을 작성하시오.

n, m = map(int, input().split())
grade_to_idx = {'A':0, 'B':1, 'C':2, 'D':3, 'F':4}
arr = [list(map(lambda x: grade_to_idx[x], list(input()))) for _ in range(n)]

price = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]
]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        
        if i+1 < n and j+1 < n:
            dp[i][j] = max(dp[i][j], price[arr[i][j]][arr[i+1][j]], price[arr[i][j]][arr[i][j+1]])
        elif i+1 < n:
            dp[i][j] = max(dp[i][j], price[arr[i][j]][arr[i+1][j]])
        elif j+1 < n:
            dp[i][j] = max(dp[i][j], price[arr[i][j]][arr[i][j+1]])

print(dp)