# https://www.acmicpc.net/problem/12100

# 풀이) dfs - 다시풀기 ㅠ
# 상하좌우가 아니라, 90도씩 돌리고 무조건 왼쪽에다가 합친다

import copy

# 90도 돌리기
def rotate(arr):
    res = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = arr[i][j]
    return res

# 합치기
def convert(arr):
    res = [i for i in arr if i != 0]
    for i in range(1, len(res)):
        if res[i-1] == res[i]:
            res[i-1] *= 2
            res[i] = 0
    res = [i for i in res if i != 0]
    return res + [0] * (n - len(res))

# DFS
def dfs(arr, cnt):
    result = max([max(i) for i in arr])

    if cnt == 0:
        return result

    # 90도씩 4번 돌리기
    for _ in range(4):
        new_arr = [convert(i) for i in arr]
        result = max(result, dfs(new_arr, cnt-1))
        arr = rotate(arr)

    return result

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


print(dfs(arr, 5))