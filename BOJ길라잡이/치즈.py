# https://www.acmicpc.net/problem/2636
# 풀이) DFS

import sys
sys.setrecursionlimit(10**7)


import copy
n, m = map(int, input().split())
arr = []
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)


def get_cheese_cnt(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
    return cnt

def dfs(x, y, a, v):
    v[x][y] = 1
    a[x][y] = -1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if not v[nx][ny] and a[nx][ny] == 0:
                dfs(nx, ny, a, v)

    return a

    
def remove_cheese(arr, visited):
    # 공기를 찾고 -1로 채운다.
    arr = dfs(0, 0, arr, visited)

    # 치즈의 가장자리를 찾고 가장자리에 해당하는 구역을 -1으로 채움
    for i in range(n-1):
        for j in range(m-1):
            if arr[i][j] == 1: # 해당 영역이 치즈면
                if arr[i-1][j] == -1 or arr[i+1][j] == -1 or arr[i][j-1] == -1 or arr[i][j+1] == -1:
                    # 하나라도 0이면!
                    arr[i][j] = 2

    # -1과 2를 0으로 채움
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0
            if arr[i][j] == 2:
                arr[i][j] = 0
    
    return arr



t = 0
cnt = get_cheese_cnt(arr)
while True:
    arr = copy.deepcopy(arr)
    v = copy.deepcopy(visited)
    t += 1
    
    # 가장자리 찾기 & 가장자리 없애기
    arr = remove_cheese(arr, v)
    
    # 남은 치즈 개수 구하기
    tmp = get_cheese_cnt(arr)
    if tmp == 0:
        break


    cnt = tmp

print(t)
print(cnt)