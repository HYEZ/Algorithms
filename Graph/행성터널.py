# https://www.acmicpc.net/problem/2887

# 풀이) 최소신장트리 - 크루스칼 알고리즘
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

n = int(input()) # 행성의 개수
x = []
y = []
z = []

for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()


edges = []
for i in range(n-1):
    x1, y1, z1 = x[i][0], y[i][0], z[i][0]
    x2, y2, z2 = x[i+1][0], y[i+1][0], z[i+1][0]
    
    edges.append((x2-x1, x[i][1], x[i+1][1]))
    edges.append((y2-y1, y[i][1], y[i+1][1]))
    edges.append((z2-z1, z[i][1], z[i+1][1]))

parent = [0] * n
for i in range(n):
    parent[i] = i


edges.sort()
# print(edges)
res = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)