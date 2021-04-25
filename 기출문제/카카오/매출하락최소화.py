# https://programmers.co.kr/learn/courses/30/lessons/72416
# 카카오 2021 신입 공채
# 풀이) DP + DFS

def dfs(sales, root):
    global graph, dp, visited
    n = len(sales)
    INF = int(1e9)

    # root가 리프노드이면 (자식노드가 없으면) => 자기 매출액 리턴
    if len(graph[root]) == 0:
        dp[root][1] = sales[root] # 리프노드가 참석하는경우
        dp[root][0] = 0 # 리프노드가 참석 안하는 경우
        return dp[root]

    sum_child = 0
    is_attend = False
    min_value = INF

    for i in graph[root]: # 자식노드 탐방

        if not visited[i]:
            visited[i] = True
            dp[i] = dfs(sales, i)
            sum_child += min(dp[i][0], dp[i][1]) # 자식노드들 최소값 합

            if dp[i][0] > dp[i][1]: 
                is_attend = True

            min_value = min(min_value, dp[i][1] - dp[i][0])

    dp[root][1] = sales[root] + sum_child
    if is_attend:
        # 이경우엔 sum_child에서 dp[i][1]이 한번이상 더해짐 -> 즉, 자식노드가 워크숍에 참석했다!
        dp[root][0] = sum_child
    else:
        # 이경우엔 자식노드가 워크숍에 참석 x -> 강제로 하나의 노드를 참석시켜야함
        # 매출 손해가 작도록 (참석했을때 매출액 - 참석안했을때 매출액)이 최소인 자식을 참석시킴 
        dp[root][0] = sum_child + min_value

    return dp[root]


def solution(sales, links):
    global graph, dp, visited
    INF = int(1e9)
    n = len(sales)
    visited = [False] * (n+1)

    graph = [[] for _ in range(n+1)]
    dp = [[0, 0] for _ in range(n+1)] # i번 노드가 참석할경우, 불참할경우에 대한 최적해
    sales = [0] + sales
    
    for a, b in links:
        graph[a].append(b)

    for i in range(1, n+1):
        visited[i] = True
        dfs(sales, i) 

    return min(dp[1])


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]	
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]	

print(solution(sales, links))