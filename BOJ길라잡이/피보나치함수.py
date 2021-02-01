# https://www.acmicpc.net/problem/1003
# 풀이) 전역변수 
import sys
sys.setrecursionlimit(10**7)

c0, c1 = 0, 0
def fibonacci(n):
    global c0, c1
    if n == 0:
        c0 += 1
        return 0
    elif n == 1:
        c1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

t = int(input())
for _ in range(t):
    n = int(input())
    c0, c1 = 0, 0
    fibonacci(n)
    print(c0, c1)

