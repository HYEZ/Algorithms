# 이것이 코딩테스트다

T = int(input())
Mt = [0 for _  in range(T)]
N, M = [0]*T, [0]*T
for t in range(T):
    N[t], M[t] = map(int, input().split())
    arr = list(map(int, input().split()))
    Mt[t] = [[] for _ in range(N[t])]
    print(Mt)
    for i in range(N[t]):
            Mt[t][i] = arr[i*M[t]:i*M[t]+M[t]]

dx = [1, 1, 1]
dy = [-1, 0, 1]

for t in range(T):
    n, m = N[t], M[t]
    matrix = Mt[t]
    print(matrix)
    dp = [[0]*n for _ in range(m)]
    
    for i in range(n):
        dp[0][i] = matrix[i][0] # dp 테이블에 첫번째 열 채움
    dp = matrix.copy()
    
    # m 번 이동함
    for i in range(1, m):
        for j in range(n):
            k = []
            if j-1 < 0:
                k = [dp[i-1][j], dp[i-1][j+1]]
            elif j+1 >= n:
                k = [dp[i-1][j-1], dp[i-1][j]]
            else:
                k = [dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]]
            dp[i][j] = max(k) + matrix[j][i]

    print(dp)
    print(max(dp[-1]))





# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

