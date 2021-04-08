# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


            
def solution(n, computers):
    c = [[] for _ in range(n)]
    visited = [False]*n # 방문노드 체크

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                c[i].append(j)
    print(c)
    answer = 0

    for i in range(n):
        if dfs(c, i, visited) == True:
            answer += 1

    return answer     

def dfs(graph, v, visited):
    if visited[v] == True:
        return False

    visited[v] = True
    # print('v: ', v, end=' ')
    
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return True



n = 3 # 컴퓨터 개수
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # computers[i][j] = 1 : 컴퓨터 i, j 가 연결되어있음
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(solution(n, computers))


