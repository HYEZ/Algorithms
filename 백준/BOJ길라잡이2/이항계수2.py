# https://www.acmicpc.net/problem/11051
# 풀이) 

# 이항계수 : nCk


n, k = map(int, input().split())

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if n < k:
    print(0)
else:
    c= 'n! / k!(n-1)!'
    c = factorial(n) // (factorial(k) * factorial(n-k))
    print(c%10007)
