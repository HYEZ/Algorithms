# https://www.acmicpc.net/problem/19236
# 삼성전자 2020 상반기 공채 - 다시풀기!
# 풀이) dfs

import copy

n = 4
fish = [[0]*n for _ in range(n)]

answer = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


for i in range(n):
    data = list(map(int, input().split()))
    for j in range(0, len(data), 2):
        fish[i][j//2] = [data[j], data[j+1]-1] # 물고기 번호, 물고기 방향


def find_fish(fish, k):
    for i in range(n):
        for j in range(n):
            if fish[i][j][0] == k:
                return (i, j)
    return None

def turn_left(direction):
    return (direction + 1) % 8

def move_fish(fish, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(fish, i) # 해당 물고기 위치 찾기
        if position != None:
            x, y = position
            direction = fish[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    if not (nx == now_x and ny == now_y):
                        fish[x][y][1] = direction
                        fish[x][y], fish[nx][ny] = fish[nx][ny], fish[x][y] # swap
                        break
                direction = turn_left(direction)


def get_position(fish, now_x, now_y):
    position = []
    direction = fish[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if now_x >= 0 and now_y >= 0 and now_x < n and now_y < n:
            if fish[now_x][now_y][0] != -1:
                position.append((now_x, now_y))
    return position

def dfs(fish, now_x, now_y, total):
    global answer
    fish = copy.deepcopy(fish)

    total += fish[now_x][now_y][0]
    fish[now_x][now_y][0] = -1
    
    move_fish(fish, now_x, now_y) # 물고기 이동
    position = get_position(fish, now_x, now_y) # 상어가 이동할 수 있는 위치

    if len(position) == 0: # 상어 이동 못하면 return
        answer = max(answer, total)
        return

    for next_x, next_y in position:
        dfs(fish, next_x, next_y, total) # 상어 이동

dfs(fish, 0, 0, 0)
    
print(answer)