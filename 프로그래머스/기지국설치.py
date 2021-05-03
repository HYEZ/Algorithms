# https://programmers.co.kr/learn/courses/30/lessons/12979
# 풀이) 구현


# 구현 : 효율성 실패 (visited 배열 때문..)
def solution(n, stations, w):
    # visited 초기화
    visited = [0] * n
    for x in stations:
        x -= 1
        start = x - w
        if start < 0:
            start = 0
        end = x + w + 1
        if end > n:
            end = n
        for i in range(start, end):
            visited[i] = 1
            

    cnt = 0
    c = w*2 + 1 # 한번에 연속적으로 방문하는 개수
    i = 0

    while i < n:
        if visited[i]:
            i += 1
            continue
        i += c
        cnt += 1
        # print(i, cnt, visited)
    

    return cnt


        
n, stations, w = 11,	[4, 11],	1
# n, stations, w = 16, [9], 2

print(solution(n, stations, w))