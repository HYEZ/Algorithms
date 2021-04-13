# https://programmers.co.kr/learn/courses/30/lessons/49994
# 풀이) 구현

# 처음 방문한 길의 길이 구하기
def solution(dirs):
    dirs = list(dirs)
    x, y = 5, 5 # start
    visited = set()

    dirs_to_idx = {'U':0, 'D':1, 'R':2, 'L':3}
    dirs = list(map(lambda x: dirs_to_idx[x], dirs))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0
    for d in dirs:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx > 10 or ny > 10 or nx < 0 or ny < 0:
            continue
        
        step1 = (x, y, nx, ny)
        step2 = (nx, ny, x, y)

        if step1 not in visited:
            visited.add(step1)
            visited.add(step2)
            cnt += 1

        x = nx
        y = ny 
    
    return cnt
     


dirs = 'LULLLLLLU'
# dirs = 'LULLLLLLU'
print(solution(dirs))