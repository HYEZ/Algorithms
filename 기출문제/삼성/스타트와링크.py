# https://www.acmicpc.net/problem/14889
# 풀이) 완전탐색
from itertools import combinations
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

users = range(n)
comb = list(combinations(users, n//2))

team = [[c, tuple(set(users) - set(c))] for c in comb[:len(comb)//2]]

res = int(1e9)
for x, y in team:
    x_score = 0
    for i, j in list(combinations(x, 2)):
        x_score += arr[i][j] + arr[j][i]

    y_score = 0
    for i, j in list(combinations(y, 2)):
        y_score += arr[i][j] + arr[j][i]

    res = min(res, abs(x_score - y_score))
    
print(res)
