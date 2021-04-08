# https://www.acmicpc.net/problem/11051
# 풀이) 구현

n, k = map(int, input().split())

def factorial(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

if n < k:
    print(0)
else:
    c = factorial(n) // (factorial(k) * factorial(n-k))
    print(c%10007)