from collections import deque
import copy

def solution(n, m, board):
    
    board = list(map(list, board))
    while True:
        visited = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    visited[i][j] = 1

        # print('board', board)
        for i in range(n-1):
            for j in range(m-1):
                # v = copy.deepcopy(visited)
                # board = copy.deepcopy(board)
                visited = bfs(board, i, j, visited)            
        # print('visited', visited)
        new_board = make_block(board, visited)
        # print('new_board', new_board)
        cnt1, cnt2 = 0, 0
        for x in range(n):
            cnt1 += board[x].count(0)
            cnt2 += new_board[x].count(0)
        # print(cnt1, cnt2)
        
        if cnt1 == cnt2:
            # for k in range(n):
            #     print(board[k])
            # print(board.count(0))
            return cnt1

        # print(visited)
        board = new_board


    # for i in range(n):
    #     print(board[i])

    # for i in range(n):
    #     print(visited[i])

def bfs(board, x, y, visitied):
    
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    q = deque([(x, y)])
    
    while q:
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

def make_block(board, visited):
    board = copy.deepcopy(board)
    for i in range(len(board[0])):
        idx = 0
        value = []
        for j in range(len(board)):
            
            if board[j][i] != 0:
                value.append(board[j][i]) 
            # print(visited)
            if visited[j][i] == 1 and board[j][i] != 0:
                value.pop()
                idx = j
            
            if idx != 0 and visited[j][i] == 0:
                break
            # print(visited[j][i], end=' ')
        
        # print(idx, value)
        if idx + 1 >= len(board):
            idx -= 1

        if idx != 0: #  and idx+1 < len(board)
            for j in range(idx+1, -1, -1):
                if len(value) == 0:
                    board[j][i] = 0   
                else: 
                    v = value.pop()
                    board[j][i] = v  
            
    
    return board




m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']	

# m = 6
# n = 6
# board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
print(solution(m, n, board))            