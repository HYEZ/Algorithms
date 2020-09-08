import collections

def solution(p, c):
    d = dict(collections.Counter(x for x in p))

    for i in c:
        d[i] -= 1

    for key, val in d.items():
        if val >= 1:
            return key

import collections


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
print(solution2(['leo', 'kiki', 'eden'], ['kiki', 'eden']))

print('test')