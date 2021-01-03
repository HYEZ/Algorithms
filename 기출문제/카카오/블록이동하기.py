# https://programmers.co.kr/learn/courses/30/lessons/60063 
# 카카오 2020 신입 공채
# 풀이) 다익스트라 - 다시풀기

# 목표 : (1, 1) => (n, n) : (0, 0) => (n-1, n-1)
# 오른쪽, 아래만 이동해도됨
# 한칸 이동, 90도 회전 가능
# 회전 : 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 함 == 4칸이 모두 0이여야함


import heapq

def solution(board):
    n = len(board)
    INF = int(1e9)

    dx = [1, 0]
    dy = [0, 1]

    start = [(0, 0), (0, 1)]
    
    distance = [[INF]*n for _ in range(n)]
    distance[0][0] = 1
    distance[0][1] = 1

    q = []
    heapq.heappush(q, (1, 1, start))
    visited = set()

    while q:
        dist1, dist2, (now1, now2)  = heapq.heappop(q)
        print(dist1, dist2, now1, now2)
        if distance[now1[0]][now1[1]] < dist1:
            continue

        if distance[now2[0]][now2[1]] < dist2:
            continue
        
        # 이동 
        for k in range(2): 
            i1, j1 = now1[0] + dx[k], now1[1] + dy[k]
            i2, j2 = now2[0] + dx[k], now2[1] + dy[k]

            if i1 < 0 or j1 < 0 or i1 >= n or j1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n:
                continue
            if board[i1][j1] == 1 or board[i2][j2] == 1:
                continue
            
            
            cost1 = dist1 + 1
            cost2 = dist2 + 1

            if ((i1, j1), (i2, j2)) not in visited:
                heapq.heappush(q, (cost1, cost2, [(i1, j1), (i2, j2)]))
                distance[i1][j1] = cost1
                distance[i2][j2] = cost2
                visited.add(((i1, j1), (i2, j2)))

            # if cost < distance[i1][j1] or cost < distance[i2][j2]:
            #         heapq.heappush(q, (cost, [(i1, j1), (i2, j2)]))
            # if cost < distance[i1][j1]:
            #     distance[i1][j1] = cost
            # if cost < distance[i2][j2]:
            #     distance[i2][j2] = cost
            


        # 회전
        # x 축이 같은 경우
        if now1[0] == now2[0]:
            i1, j1 = now1[0]+1, now1[1]
            i2, j2 = now2[0]+1, now2[1]
        elif now1[1] == now2[1]:
            i1, j1 = now1[0], now1[1]+1
            i2, j2 = now2[0], now2[1]+1

        if not (i1 < 0 or j1 < 0 or i1 >= n or j1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n):
            if board[i1][j1] == 0 and board[i2][j2] == 0:
                # 왼쪽회전 
                # cost = distance[now1[0]][now1[1]] + 1
                cost1 = dist1 + 1
                cost2 = dist2 + 1
                if cost1 <= distance[i1][j1] and  (now1, (i1, j1)) not in visited:
                    print('   >',cost1, now1, i1, j1)
                    visited.add((now1, (i1, j1)))
                    heapq.heappush(q, (cost1, cost2, [now1, (i1, j1)]))
                    distance[i1][j1] = cost1

                # 오른쪽회전
                # cost = distance[now2[0]][now2[1]] + 1
                # cost = dist2 + 1
                if cost2 <= distance[i2][j2] and  (now2, (i2, j2)) not in visited: 
                    print('   >', cost2, now2, i2, j2)
                    visited.add((now2, (i2, j2)))
                    heapq.heappush(q, (cost1, cost2, [now2, (i2, j2)]))
                    distance[i2][j2] = cost2
                    
      

    print(distance)
    return distance[n-1][n-1] - 1

        
        

        # # x 축이 같은 경우
        # if now1[0] == now2[0]:
        #     # 왼쪽 회전 => now1을 고정, now2의 좌표만 바꾼다.
        #     i1, j1 = now1
        #     i2, j2 = i1+1, j1

        #     if not (i1+1 < 0 or j1+1 < 0 or i1+1 >= n or j1+1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n): # 공반 밖도 아니고
        #         if not (board[i2][j2] == 1 or board[i1+1][j1+1] == 1):
        #             # print(i1, j1, i2, j2)
        #             distance = update_distance(q, distance, i1, i2, j1, j2, dist+1)

        #     # 오른쪽 회전 => now2을 고정, now1의 좌표만 바꾼다. 그리고 now2를 now1로 바꿈
        #     i1, j1 = now2
        #     i2, j2 = i1+1, j1

        #     if not (i1+1 < 0 or j1-1 < 0 or i1+1 >= n or j1-1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n): # 공반 밖도 아니고
        #         if not (board[i2][j2] == 1 or board[i1+1][j1-1] == 1):
        #             # print(i1, j1, i2, j2)
        #             distance = update_distance(q, distance, i1, i2, j1, j2, dist+1)
            
        
        # # y 축이 같은 경우
        # elif now1[1] == now2[1]:
        #     # 왼쪽 회전 => now1을 고정, now2의 좌표만 바꾼다.
        #     i1, j1 = now1
        #     i2, j2 = i1, j1+1

        #     if not (i1+1 < 0 or j1+1 < 0 or i1+1 >= n or j1+1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n): # 공반 밖도 아니고
        #         if not (board[i2][j2] == 1 or board[i1+1][j1+1] == 1):
        #             # print(i1, j1, i2, j2)
        #             distance = update_distance(q, distance, i1, i2, j1, j2, dist+1)

        #     # 오른쪽 회전 => now2을 고정, now1의 좌표만 바꾼다. 그리고 now2를 now1로 바꿈
        #     i1, j1 = now2
        #     i2, j2 = i1, j1+1

        #     if not (i1-1 < 0 or j1+1 < 0 or i1-1 >= n or j1+1 >= n or i2 < 0 or j2 < 0 or i2 >= n or j2 >= n): # 공반 밖도 아니고
        #         if not (board[i2][j2] == 1 or board[i1-1][j1+1] == 1):
        #             # print(i1, j1, i2, j2)
        #             distance = update_distance(q, distance, i1, i2, j1, j2, dist+1)

        

    
    

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
print(solution(board))





