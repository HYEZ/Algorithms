# https://www.acmicpc.net/problem/1976
# 풀이) 서로소 집합 알고리즘

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a

n = int(input())
m = int(input()) # 여행계획에 속한 도시들의 수 
arr = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(lambda x: int(x)-1, input().split()))
parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union_parent(parent, i, j)

res = [find_parent(parent, plan[i]) for i in range(m)]
if len(list(set(res))) == 1:
    print('YES')
else:
    print('NO')




