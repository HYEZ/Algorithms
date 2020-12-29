# https://www.acmicpc.net/problem/19237
# 삼성전자 2020 상반기 공채
# 풀이) 구현 - 다시풀기!

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

smell = [[[0, 0]]*n for _ in range(n)]
directions = list(map(int, input().split())) # 각 상어의 방향

priorities = []
for _ in range(m):
    data = []
    for _ in range(4):
        data.append(list(map(int, input().split()))) # 위, 아래, 왼, 오 각각 우선순위
    priorities.append(data)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def set_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]

# 상어가 이동함
def move():
    new_arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:
                direction = directions[arr[x][y] - 1] # 현재 상어의 방향
                found = False
                for i in range(4):
                    nx = x + dx[priorities[arr[x][y] - 1][direction - 1][i]-1] ###
                    ny = y + dy[priorities[arr[x][y] - 1][direction - 1][i]-1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][i]

                            if new_arr[nx][ny] == 0:
                                new_arr[nx][ny] = arr[x][y]
                            else:
                                new_arr[nx][ny] = min(new_arr[nx][ny], arr[x][y])

                            found = True 
                            break
                if found:
                    continue

                for i in range(4):
                    nx = x + dx[priorities[arr[x][y] - 1][direction - 1][i]-1] ###
                    ny = y + dy[priorities[arr[x][y] - 1][direction - 1][i]-1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if smell[nx][ny][0] == arr[x][y]:
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][i]
                            new_arr[nx][ny] = arr[x][y]
                            break 
    return new_arr


t = 0
while True:
    set_smell()
    arr = move()
    t += 1

    chk = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                chk = False
    if chk:
        print(t)
        break

    if t >= 1000:
        print(-1)
        break
