# https://programmers.co.kr/learn/courses/30/lessons/17679
# 카카오 2018 신입 공채 1차
# 풀이) 구현, 완전탐색, 스택
# 참고) BFS로 풀었더니 시간초과남 (맨 아래 코드)

from collections import deque
import copy

def solution(n, m, board):
    board = list(map(list, board))
    answer = 0
    while True:
        visited = [[0] * m for _ in range(n)]   

        visited, cnt = chk_visited(n, m, board, visited)
        if cnt == 0:
            break

        board = make_block(board, visited)

    for x in range(n):
        answer += board[x].count(0)

    return answer

def chk_visited(n, m, board, visitied):
    res = []
    for i in range(n-1): 
        for j in range(m-1):
            tmp = board[i][j]
            if tmp == 0:
                continue
            if board[i+1][j] == tmp and board[i][j+1] == tmp and board[i+1][j+1] == tmp:
                visitied[i][j] = 1
                visitied[i+1][j] = 1
                visitied[i][j+1] = 1
                visitied[i+1][j+1] = 1
                res += [board[i+1][j], board[i][j+1], board[i+1][j+1]]
    
    return visitied, len(res)



def make_block(board, visited):    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited[i][j] == 1:
                board[i][j] = 0

    
    for i in range(len(board[0])):
        value = []
        for j in range(len(board)):
            if board[j][i] != 0:
                value.append(board[j][i])

        for j in range(len(board) - 1, -1, -1):
            if len(value) > 0:
                v = value.pop()
                board[j][i] = v
            else:
                board[j][i] = 0

    return board

    


m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']	

# m = 6
# n = 6
# board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
n = 6
m = 5
board = ['AAAAAA', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA']

# # 답 32
# n = 6
# m = 6
# board = ['AABBEE','AAAEEE','VAAEEV','AABBEE','AACCEE','VVCCEE' ]

n = 4
m = 4

board = ['ABCD', 'BACE', 'BCDD', 'BCDD']



print(solution(m, n, board))            


def bfs(board, x, y, visitied):
    
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    q = deque([(x, y)])
    
    while q: #100
        x, y = q.popleft()

        chk = 3
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= len(visitied) or ny >= len(visitied[0]):
                chk -= 1
                continue
            if board[x][y] == board[nx][ny]:
                chk -= 1

        if chk == 0:
            for i in range(3):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or ny < 0 or nx >= len(visitied) or ny >= len(visitied[0]):
                    continue
                visitied[x][y] = 1
                visitied[nx][ny] = 1
                q.append((nx, ny))
    
    return visitied