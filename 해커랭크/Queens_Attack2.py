# https://www.hackerrank.com/challenges/queens-attack-2/problem
# 풀이) DFS => 효율성 문제 고치기  => 백트래킹

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


import math
def get_delta(x1, y1, x2, y2):
    delta_x = (x2-x1)
    delta_y = (y2-y1)
    if delta_x == 0 or delta_y == 0:
        return 0

    return (y2-y1)//(x2-x1)

def get_distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


def queensAttack(n, k, r_q, c_q, obstacles):
    global x, y, obs

    x, y = n-r_q+1, c_q
    # obs = {0: [x, 1], 1:[x, n], 2: [1, y], 3:[n, y], 4: [1, n], 5:[n, 1], 6: [1, 1], 7:[n, n]} # left, right, up, down, ul, dr, dl, ur
    obs = {0: [x, 0], 1:[x, n+1], 2: [0, y], 3:[n+1, y], 4: [0, n], 5:[n+1, 1], 6: [0, 0], 7:[n+1, n+1]} # left, right, up, down, ul, dr, dl, ur

   # 기울기가 0, 1, -1 인거만 담기
    for i, (a, b) in enumerate(obstacles):
        a = n-a+1
        print(a, b)
        delta_x = (x-a)
        delta_y = (y-b)
        k = -1
        if delta_x == 0 and delta_y > 0: # up
            k = 2            
        elif delta_x == 0 and delta_y < 0: # down
            k = 3
        elif delta_y == 0 and delta_x > 0: # left
            k = 0           
        elif delta_y == 0 and delta_x < 0: # right
            k = 1
        elif (delta_y)//(delta_x) == 1 and delta_x > 0: # ur
            k = 7
        elif (delta_y)//(delta_x) == 1 and delta_x < 0: # dl
            k = 6
        elif (delta_y)//(delta_x) == -1 and delta_x < 0: # ul
            k = 4
        elif (delta_y)//(delta_x) == 1 and delta_x > 0: # dr
            k = 5 

        if k != -1:
            if get_distance(x, y, obs[k][0], obs[k][1]) > get_distance(x, y, a, b):
                obs[k][0] = a
                obs[k][1] = b

    print(obs)
    answer = 0
    for k in range(8):
        print(abs(obs[k][0]-x), abs(obs[k][1]-y))
        answer += abs(obs[k][0]-x) + abs(obs[k][1]-y) - 3


    # for i in range(8):
    #     answer += backtrack_dfs(x, y, i, 0)

    return answer


def is_possible(nx, ny):
    global x, y, obs
    if nx >= 1 and ny >= 1 and nx <= n and ny <= n:
        for i, (a, b) in enumerate(obs):
            if nx == a and ny == b:                
                return False
        return True
    return False
    


def backtrack_dfs(x, y, i, cnt):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # left, right, up, down, ul, dr, dl, ur
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