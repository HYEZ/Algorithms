# https://programmers.co.kr/learn/courses/30/lessons/12939
# 풀이) min, max

def solution(s):
    s = list(map(int, s.split()))
    res = ''.join(str(min(s)) + ' ' + str(max(s)))
    return res

s = "-1 -2 -3 -4"
print(solution(s))