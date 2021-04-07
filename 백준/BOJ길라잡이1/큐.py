# https://www.acmicpc.net/problem/10845
# 풀이) 큐

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    data = input().split()
    op = data[0]
    if op == 'push':
        q.append(data[1])
    elif op == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif op == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif op == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
