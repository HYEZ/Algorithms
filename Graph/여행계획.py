# 이것이 코딩테스트다
# 풀이) 서로소집합 알고리즘

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
graph = [[] for _ in range(n+1)]
for j in range(1, n+1):
    data = list(map(int, input().split()))
    for i, d in enumerate(data):
        if d == 1:
            graph[j].append(i+1)

plan = list(map(int, input().split()))

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    for j in range(len(graph[i])):
        union_parent(parent, i, graph[i][j])

# print(graph, parent)

res = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        res = False

print(res)
    

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0 
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3