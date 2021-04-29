# https://programmers.co.kr/learn/courses/30/lessons/12953
# 풀이) 스택

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    answer = 1

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]




arr = [2,6,8,14]	
arr = [1, 2, 3]
print(solution(arr))