# https://www.acmicpc.net/problem/14891
# 삼성 SW 역량 테스트
# 풀이) 구현, DFS

import sys
sys.setrecursionlimit(10**8)


arr = []
for _ in range(4):
    data = list(map(int, list(input())))
    arr.append(data)

k = int(input())
op = []
for _ in range(k):
    idx, d = map(int, input().split())
    op.append((idx-1, d))

indexes = [2, 6, 2, 6]

def rotate(a, d):
    if d == 1: # 시계방향
        a = [a[-1]] + a[:-1]
    else: # 반시계 방향
        a = a[1:] + [a[0]]

    return a


def dfs(arr, i, d, visited):
    visited[i] = 1
    if i-1 >= 0:
        if not visited[i-1]:
            if arr[i][6] != arr[i-1][2]:
                dfs(arr, i-1, d*-1, visited)

    if i+1 <= 3:
        if not visited[i+1]:
            if arr[i+1][6] != arr[i][2]:
                dfs(arr, i+1, d*-1, visited)

    arr[i] = rotate(arr[i], d)


for i, d in op:
    visited = [0, 0, 0, 0]
    dfs(arr, i, d, visited)

print(sum([x[0]*(2**i) for i, x in enumerate(arr)]))