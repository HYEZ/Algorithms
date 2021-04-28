# https://programmers.co.kr/learn/courses/30/lessons/67260
# 카카오 2020 인턴쉽
# 풀이) DFS

import sys
sys.setrecursionlimit(10**7)

def dfs(now):
    global graph, priority, post_order, visited

    if not visited[now] and (pre_order[now] == 0 or visited[pre_order[now]]): 
        # print(now)
        visited[now] = True
        for i in graph[now]:
            dfs(i)

        if post_order[now] != 0:
            dfs(post_order[now])


def solution(n, path, order):
    global graph, pre_order, post_order, visited

    pre_order = [0] * n # each 방을 방문하기 전에 꼭 방문해야하는 방 번호
    post_order = [0] * n 
    for a, b in order:
        pre_order[b] = a
        post_order[a] = b

    visited = [False] * n
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    if pre_order[0] != 0: #  입구에 선방문이 존재하는 경우
        return False
    
    visited[0] = True
    for i in graph[0]:
        dfs(i)
    
    # print(visited)

    return n == sum(visited)



n, path, order = 9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]]
n, path, order = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]
n, path, order = 9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]	, [[4,1],[5,2]]	
print(solution(n, path, order))