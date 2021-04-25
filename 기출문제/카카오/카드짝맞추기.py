# https://programmers.co.kr/learn/courses/30/lessons/72415
# 카카오 2021 신입 공채
# 풀이) BFS, backtracking

from itertools import permutations
from collections import deque
from collections import defaultdict
                
INF = int(1e9)
n = 4
myboard = [[] for i in range(n)]
orders = [] # 카드 순서 (순열)
location = defaultdict(list) # 카드가 있는 좌표
answer = INF

# 카드 1장을 찾을 때 나오는 거리, 목표위치를 반환하는 함수
def bfs(sx, sy, ex, ey): # start 좌표, end 좌표
    global myboard

    if [sx, sy] == [ex, ey]: # 시작위치와 목표위치가 같으면 리턴
        return sx, sy, 1

    dp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q = deque([[sx, sy]])
    visited[sx][sy] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            # 한칸이동
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dp[nx][ny] = dp[x][y] + 1
                    if [nx, ny] == [ex, ey]:
                        return  nx, ny, dp[nx][ny] + 1
                    q.append([nx, ny])
            
            # ctrl + 방향키
            nx, ny = move(x, y, i) 
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dp[nx][ny] = dp[x][y] + 1
                if [nx, ny] == [ex, ey]:
                        return  nx, ny, dp[nx][ny] + 1
                q.append([nx, ny])
                
    
    return sx, sy, INF

# ctrl + 방향키 (한번에 이동)
def move(x, y, i):
    global myboard
    nx, ny = x, y

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        _nx = nx + dx[i]
        _ny = ny + dy[i]

        if _nx < 0 or _ny < 0 or _nx >= n or _ny >= n: # 범위 밖이면
            return nx, ny
        
        if myboard[_nx][_ny] != 0: # 카드가 있는곳이면
            return _nx, _ny
        
        nx = _nx
        ny = _ny
            


# 찾은 2장의 카드를 mybord에서 지워주는 함수
def remove(card):
    global myboard, location
    for x, y in location[card]:
        myboard[x][y] = 0

# 지운 2장의 카드를 mybord에서 복원하는 함수
def restore(card):
    global myboard, location
    for x, y in location[card]:
        myboard[x][y] = card


def backtrack(sx, sy, i, j, cnt):
    global orders, location, answer

    if j == len(location.keys()): # 현재 순서에서 다 봤으면
        if answer > cnt:
            answer = cnt # 최소값으로 저장
        return

    card = orders[i][j] # 현재 선택된 카드
    lx, ly = location[card][0][0], location[card][0][1] # 현재 선택된 카드의 첫번째 좌표
    rx, ry = location[card][1][0], location[card][1][1] # 현재 선택된 카드의 두번째 좌표


    # 첫번째 카드먼저 방문
    x1, y1, res1 = bfs(sx, sy, lx, ly)
    x2, y2, res2 = bfs(x1, y1, rx, ry) 

    remove(card) # 카드 방문했으면 제거
    backtrack(x2, y2, i, j+1, cnt+res1+res2) # 다음 카드 방문하려고 backtracking
    restore(card)

    # 두번째 카드먼저 방문
    x1, y1, res1 = bfs(sx, sy, rx, ry)
    x2, y2, res2 = bfs(x1, y1, lx, ly) 

    remove(card)
    backtrack(x2, y2, i, j+1, cnt+res1+res2) 
    restore(card)


def solution(board, r, c): # 보드, 커서 최초위치 row, col
    global orders, location, myboard, answer

    # 카드 위치 딕셔너리
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                location[board[i][j]].append((i, j))
            myboard[i].append(board[i][j])

    orders = list(map(list, permutations(location.keys())))

    # 백트래킹
    for i in range(len(orders)):
        backtrack(r, c, i, 0, 0)
        
    return answer

board,	r,	c = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0
print(solution(board, r, c))