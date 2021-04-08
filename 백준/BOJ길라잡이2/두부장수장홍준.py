# https://www.acmicpc.net/problem/1657
# 풀이) DP (아직 푸는중~, 나중에 다시 풀자)

n, m = map(int, input().split())
grade_to_idx = {'A':0, 'B':1, 'C':2, 'D':3, 'F':4}
arr = [list(map(lambda x: grade_to_idx[x], list(input()))) for _ in range(n)]

price = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]
]
dp = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        pass

print(dp)