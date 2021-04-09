# https://programmers.co.kr/learn/courses/30/lessons/68936
# 풀이) 재귀

import sys
sys.setrecursionlimit(10**6)

def solution(arr):
    global res
    res = [0, 0]
    divide(arr)
    return res

def get_count(arr):
    global res
    for i in range(len(arr)):
        res[0] += arr[i].count(0)
        res[1] += arr[i].count(1)
    return res

def is_same(arr):
    res = 0
    n = len(arr)
    for i in range(len(arr)):
        res += sum(arr[i])
    
    if res == n*n or res == 0:
        return True

    return False


def divide(arr):
    global res
    n = len(arr)
    if is_same(arr):
        res[arr[0][0]] += 1
        return True
    if n == 2:
        get_count(arr)
        return True
    else:
        tmp1 = [[arr[i][j] for j in range(0, n//2)] for i in range(0, n//2)]
        tmp2 = [[arr[i][j] for j in range(0, n//2)] for i in range(n//2, n)]
        tmp3 = [[arr[i][j] for j in range(n//2, n)] for i in range(0, n//2)]
        tmp4 = [[arr[i][j] for j in range(n//2, n)] for i in range(n//2, n)]
        divide(tmp1)
        divide(tmp2)
        divide(tmp3)
        divide(tmp4)


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	
arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))