# 이것이 코딩테스트다

# 풀이) 최소신장트리 - 크루스칼 알고리즘


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

n, m = map(int, input().split())
edges = []
total = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    total += z

parent = [0]*n
for i in range(n):
    parent[i] = i

edges.sort()

res = 0
for e in edges:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)    
        res += cost
        
print(total-res)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11
