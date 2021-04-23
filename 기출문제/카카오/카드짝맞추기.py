# https://programmers.co.kr/learn/courses/30/lessons/72415
# 카카오 2021 신입 공채
# 풀이) BFS

from itertools import permutations
from collections import deque
from collections import defaultdict

# def bfs(board, r, c, case):
#     d = dict()
#     for i in case:
#         d[i] = 0

#     visited = [[0] * 4 for _ in range(4)]
#     q = deque([(r, c)])

#     if board[r][c] != 0:
#         d[board[r][c]] = 1

#     visited[r][c] = 1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, -1, 1]
#     k = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x, y
#             for j in range(4):
#                 nx = nx + dx[i]
#                 ny = ny + dy[i]
#                 if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:              
                    
#                     if k < len(case) and board[nx][ny] == case[k]:
#                         if d[case[k]] <= 1:
#                             if not visited[nx][ny]:
#                                 k += d[case[k]]
#                                 d[case[k]] += 1 
#                                 q.append((nx, ny))
#                     elif (nx == 0 and ny == 0) or (nx == 0 and ny == 3) or (nx == 3 and ny == 0) or (nx == 3 and ny == 3):
#                         if not visited[nx][ny]:
#                             q.append((nx, ny))
#                             visited[nx][ny] = 1
                        
#     print(d)
                



def solution(board, r, c): # 보드, 커서 최초위치 row, col
    arr = sorted(list(set([board[i][j] for j in range(4) for i in range(4)])))
    arr.remove(0)
    cases = list(map(list, permutations(arr)))
    
    location = defaultdict(list)
    start = (r, c)
    
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                location[board[i][j]].append((i, j))

    print(location)
    
    for case in cases:
        # bfs(board, r, c, case)
        print(case)
    # case = 

    pass



board,	r,	c = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0
print(solution(board, r, c))