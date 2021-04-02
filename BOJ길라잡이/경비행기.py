# https://www.acmicpc.net/problem/2585
# 풀이) 최단거리

import math
n, k = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())

s = (0, 0)
t = (10000, 10000)

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def feul(dist):
    return math.ceil(dist*0.1)


print(feul(54.671))