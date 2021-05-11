# https://www.hackerrank.com/challenges/queens-attack-2/problem
# 풀이) DFS => 효율성 문제 고치기  => 백트래킹

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def queensAttack(n, k, r_q, c_q, obstacles):
    global x, y, row, col
    answer = 0
    x, y = r_q, c_q
    row = [[] for _ in range(n+1)]
    col = [[] for _ in range(n+1)]
    for i, a in enumerate(obstacles):
        a, b = a
        row[a].append(i)
        col[b].append(i)


    for i in range(8):
        answer += backtrack_dfs(x, y, i, 0)

    return answer


def is_possible(nx, ny):
    global x, y, row, col
    if nx >= 1 and ny >= 1 and nx <= n and ny <= n:
        for i in row[nx]:
            for j in col[ny]:
                if i == j:
                    return False
        
        return True
    return False
    


def backtrack_dfs(x, y, i, cnt):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    nx = x + dx[i]
    ny = y + dy[i]

    if is_possible(nx, ny):
        cnt += backtrack_dfs(nx, ny, i, 1)
        

    return cnt
    
   

n, k = map(int, input().split())
r_q, c_q  = map(int, input().split())
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().split())))

print(queensAttack(n, k, r_q, c_q, obstacles))