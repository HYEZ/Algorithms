# https://www.acmicpc.net/problem/1717
# 풀이) 서로소 집합 알고리즘

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
arr = []
for _ in range(m):
    op, a, b = map(int, input().split())
    arr.append((op, a, b))

# 특정한 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


for op, a, b in arr:
    if op == 0: # 합집합
        union_parent(parent, a, b)
    elif op == 1: # 같은 집합인지 확인
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print('YES')
        else:
            print('NO')