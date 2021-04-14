# https://www.acmicpc.net/problem/4195s
# 풀이) 서로소 집합 알고리즘

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict, Counter

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = a
        num[a] += num[b]

t = int(input())
for _ in range(t): # test case
    n = int(input()) # 친구 관계 수
    
    parent = defaultdict(str)
    num = defaultdict(int)
    
    for _ in range(n):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            num[a] = 1
    
        if b not in parent:
            parent[b] = b
            num[b] = 1
            
        union_parent(a, b)
        print(num[find_parent(a)])