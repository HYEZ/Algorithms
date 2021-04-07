# https://www.acmicpc.net/problem/9576
# 풀이) 그리디, 정렬

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [0] * (n+1)
    r = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        r.append((a, b))

    r.sort(key=lambda x:(x[1], x[0]))

    for a, b in r:
        for i in range(1, n+1):
            if a <= i <= b and arr[i] == 0:
                arr[i] = 1
                break

    print(sum(arr))
