# https://www.acmicpc.net/problem/19236
# 삼성전자 2020 상반기 공채

# 4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 
# 한 칸에는 물고기가 한 마리 존재한다. 
# 각 물고기는 번호와 방향을 가지고 있다. 
# 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 
# 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

# 0. 상어는 (0,0)의 물고기를 먹고 그 물고기의 방향을 갖게 됨
# 1. 물고기 먼저 이동
#     - 번호가 작은 순서대로 이동
#     - 한번에 한칸만
#     - 이동할 수 있는 칸 : 빈칸, 다른 물고기가 있는 칸
#     - 이동할 수 없는 칸 : 상어가 있는 칸, 공간의 경계를 넘어간 칸
#     - 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다
#         - 이동할 수 있으면 그 칸으로 이동함
#         - 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
#     - 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

# 2. 상어 이동
#     - 한번에 여러 칸 동시에
#     - 물고기 먹고 물고기의 방향 가지게됨
#     - 물고기 없는 칸은 이동 못함
#     - 이동할 수 없으면 집으로
# 3. 상어가 이동한 후에는 다시 물고기가 이동함 (반복)

# 4. 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.


n = 4
fish = [[0]*n for _ in range(n)]


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 
1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(0, len(data), 2):
        fish[i][j//2] = (data[j], data[j+1]-1) # 물고기 번호, 물고기 방향

# 상어가 첨에 (0,0) 먹는거
shark = [0, 0, fish[0][0][1]]
fish[0][0] = 0

print(fish)

def shift_fish(now_fish):
    # print(now_fish)
    for i in range(n):
        for j in range(n):
            if fish[i][j] != 0 and fish[i][j][0] == now_fish:
                # 물고기 방향 이동 (빈칸, 다른 물고기가 있는 칸으로)
                cur_direction = fish[i][j][1]
                for k in range(cur_direction, cur_direction+8):
                    k = k % 8
                    nx = j + dx[k]
                    ny = i + dy[k]
                    # print(k, i, j, dx[k], dy[k], nx, ny)
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if fish[ny][nx] == 0: # 상어가 있는 칸
                        continue
                    # 물고기 위치 swap
                    tmp = fish[i][j]
                    fish[i][j] = fish[ny][nx]
                    fish[ny][nx] = tmp
                    return fish
    return fish    

    
# 물고기 이동
now_fish = 1
while now_fish <= 16:
    fish = shift_fish(now_fish)
    print(fish)
    now_fish += 1


# 상어 이동