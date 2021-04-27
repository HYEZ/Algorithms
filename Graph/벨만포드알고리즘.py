# 벨만포드 알고리즘
# weight이 음수여도 동작한다. (단, 사이클의 sum of weight은 음수면 안됨!)
# 즉, 음수 가중치가 있는경우, 음수 사이클을 피해 최단 경로를 구해준다. (다익스트라는 음수 가중치 안됨)
# 단, comlexity : O(EV)


import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split()) 
start = int(input())
graph = [[] for i in range(v+1)]

distance = [INF] * (v+1)
distance[start] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 최단 경로 구하기
for _ in range(v-1):
    for i in range(v):
        for j, cost in graph[i]:
            if distance[j] > distance[i] + cost:
                distance[j] = distance[i] + cost

# 음수 사이클 존재 여부 검사
for i in range(v):
    for j, cost in graph[i]:
        if distance[j] > distance[i] + cost:
            print('no answer')
            break

print(distance[1:])

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 15
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
