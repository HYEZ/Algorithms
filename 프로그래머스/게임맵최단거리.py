# https://programmers.co.kr/learn/courses/30/lessons/1844
# 풀이) 최단거리(bfs + dp)

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dp = [[-1] * m for _ in range(n)]

    q = deque([(0, 0)])
    dp[0][0] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n and nx >= 0 and ny < m and ny >= 0:
                if maps[nx][ny] == 1 and dp[nx][ny] == -1:
                    dp[nx][ny] = dp[x][y] + 1
                    q.append((nx, ny))


    return dp[-1][-1]

    

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
print(solution(maps))