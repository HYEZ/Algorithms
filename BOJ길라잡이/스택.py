# https://www.acmicpc.net/problem/10828
# 풀이) 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    data = input().split()
    op = data[0]
    if op == 'push':
        stack.append(data[1])
    elif op == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif op == 'size':
        print(len(stack))
    elif op == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

