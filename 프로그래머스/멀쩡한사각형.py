# https://programmers.co.kr/learn/courses/30/lessons/62048
# 풀이) 그리디


from math import gcd

def solution2(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)

w = 7
h = 14
print(solution(w, h))
print(gcd(7, 14))