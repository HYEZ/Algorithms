# https://programmers.co.kr/learn/courses/30/lessons/12899
# 풀이) 구현

def solution(n):
    res = ''
    while n > 0:
        n -= 1
        res = '124'[n%3] + res
        n //= 3
    return res

    





n = 10
print(solution(n))