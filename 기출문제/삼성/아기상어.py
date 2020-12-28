# https://www.acmicpc.net/problem/16236
# 삼성전자 2020 상반기 공채 - 다시풀기!
# 풀이) bfs

from collections import deque

INF = 1e9
n = int(input()) # nxn칸의 수
space = []
shark = []

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0] 

weight = 2 # 현재 상어의 weight
t = 0 # 이동 횟수
eat = 0 # 먹은 상어 수 (weight 증가할때마다 초기화)

for _ in range(n):
    data = list(map(int, input().split()))
    space.append(data)

for i in range(n):
    for j in range(n):
        if space[i][j] == 9: # 상어
            space[i][j] = 0
            shark = [i, j]


# 최단 거리 테이블 반환
def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(shark[0], shark[1])])
    dist[shark[0]][shark[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue 

            if dist[nx][ny] == -1 and space[nx][ny] <= weight:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist


def find(dist):
    x, y  = 0, 0
    min_value = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= space[i][j] and space[i][j] < weight:
                if dist[i][j] < min_value:
                    min_value, x, y = dist[i][j], i, j

    if min_value == INF:
        return None

    return min_value, x, y
            
answer = 0

while True:
    value = find(bfs())
    if value == None:
        print(answer)
        break
    
    d, x, y = value
    answer += d
    space[x][y] = 0
    shark = [x, y]
    eat += 1
    if eat >= weight:
        weight += 1
        eat = 0






