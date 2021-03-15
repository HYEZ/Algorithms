# https://programmers.co.kr/learn/courses/30/lessons/72411
# 풀이) 완전탐색, 조합, 해쉬

# 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    types = sorted(list(set(list(''.join(orders)))))
    orders = list(map(lambda a: sorted(list(a)), orders))
    res = []
    for c in course:
        cases = list(map(lambda a: list(a), combinations(types, c)))
        print(cases)
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