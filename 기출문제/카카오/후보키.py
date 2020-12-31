# https://programmers.co.kr/learn/courses/30/lessons/42890
# 카카오 2019 신입공채
# 풀이) 완전탐색

from itertools import combinations
def solution(relation):
    answer = 0
    fields = list(range(0, len(relation[0])))
    case = list()
    for i in range(1, len(fields)+1):
        case += list(map(list,combinations(fields, i)))

    candidates = []

    for c in case:
        tmp = []
        for r in relation:
            t = []
            for i in c:
                t.append(r[i])
            tmp.append(tuple(t))
        candidates.append(tmp)

    answer = []
    for i, c in enumerate(candidates):
        chk = False
        for prev in answer:
            if set(prev).issubset(set(case[i])):
                chk = True
        if chk:
            continue
        
        if len(c) == len(set(c)):
            answer.append(case[i])

    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [
    ['a','b','c'],
    ['1','b','c'],
    ['a','b','4'],
    ['a','5','c']
]
relation = [
    ['a','1','4'],
    ['2','1','5'],
    ['a','2','4']
]
print(solution(relation))