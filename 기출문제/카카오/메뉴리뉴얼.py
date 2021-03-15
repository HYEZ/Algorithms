# https://programmers.co.kr/learn/courses/30/lessons/72411
# 풀이) 완전탐색, 조합, 해쉬

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    types = sorted(list(set(list(''.join(orders)))))
    orders = list(map(lambda a: sorted(list(a)), orders))
    res = []
    for c in course:
        cases = []
        for order in orders:
            cases += list(map(lambda a: list(a), combinations(order, c)))
        
        cases = list(set(tuple(map(tuple, cases))))

        d = defaultdict(int)
        for case in cases:
            for order in orders:
                if set(case) == set(case).intersection(set(order)):
                    key = ''.join(case)
                    d[key] += 1
        if len(d.values()) == 0:
            continue
        max_value = max(d.values())
        if max_value < 2:
            continue              
        for key, value in d.items():
            if max_value == value:
                res.append(key)
    return sorted(res)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]	
print(solution(orders, course))