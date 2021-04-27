# https://programmers.co.kr/learn/courses/30/lessons/67259
# 풀이) DP + BFS

from collections import deque

def solution(board):
    global dp, visited

    n = len(board)
    INF = int(1e9)
    dp = [[INF]*n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(0, 0, -1, 0)])
    dp[0][0] = 0
    answer = INF

    while q:
        x, y, d, c = q.popleft() # 이 때, dp[x][y]가 다른애들에 의해서 바뀌는걸 방지하기 위해 cost도 큐에 넣어야함 (그 시점의 cost와 더해주려고)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if i == d or d == -1:
                cost = c + 100
            else:
                cost = c + 600 

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == 0 and cost <= dp[nx][ny]:
                    dp[nx][ny] = cost
                    q.append((nx, ny, i, cost)) 
                    
    return dp[-1][-1]


board = [[0,0,0],[0,0,0],[0,0,0]]	
print(solution(board))