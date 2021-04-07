# https://www.acmicpc.net/problem/9466
# 풀이) 그래프(방향그래프의 싸이클 판별 => DFS)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    global team
    loop.append(x)
    visited[x] = 1    
    if not visited[arr[x]]:
        dfs(arr[x])
    else: 
        if arr[x] in loop: # 사이클 발생 => 팀 결성
            team += loop[loop.index(arr[x]):]
            return
    


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    arr = list(map(lambda x: int(x) - 1, input().split()))
    team = []
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            loop = []
            dfs(i)
    res.append(n - len(team))
            
for i in res:
    print(i)
