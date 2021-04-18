# https://www.acmicpc.net/problem/10775
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
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input()) # 게이트 수
gate = [0] * (g+1)

p = int(input()) # 비행기 수
parent = [i for i in range(g+1)]

answer = 0
for i in range(p):
    g = int(input())
    # parent를 g-1이랑 union 시켜서 0 이 되면 break
    if find_parent(parent, g) <= 0:
        break
    union_parent(parent, parent[g], parent[g]-1)
    answer += 1
    
print(answer)



    





