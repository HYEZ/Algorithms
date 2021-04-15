# https://programmers.co.kr/learn/courses/30/lessons/68645
# 풀이) DFS



import sys
sys.setrecursionlimit(10**7)

def solution(n):
    arr = [[0] * (i+1) for i in range(n)]
    arr[0][0] = 1

    # 0: 아래, 1: 오른쪽, 2: 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    def dfs(x, y, d):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < len(arr[x]) and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            dfs(nx, ny, d)
        else:
            nd = d + 1
            if d == 2:
                nd = 0
                
            nx = x + dx[nd]
            ny = y + dy[nd]
            if nx >= 0 and ny >= 0 and nx < n and ny < len(arr[x]) and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                dfs(nx, ny, nd)
            
    dfs(0, 0, 0)

    res = []
    for i in range(n):
        for j in range(len(arr[i])):
            res.append(arr[i][j])
            

    return res


n = 5
print(solution(n))
