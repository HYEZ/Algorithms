# https://programmers.co.kr/learn/courses/30/lessons/60060
# 2020 카카오 신입 공채
# 풀이) Binary Search

from bisect import bisect_left, bisect_right
from collections import defaultdict

def count_by_range(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)
    return right_idx - left_idx
    
def solution(words, queries):
    answer = []
    voca = defaultdict(list)
    voca_reverse = defaultdict(list)

    for word in words:
        voca[len(word)].append(word)
        voca_reverse[len(word)].append(word[::-1])
    
    for key, words in voca.items():
        voca[key] = sorted(words)

    for key, words in voca_reverse.items():
        voca_reverse[key] = sorted(words)


    for i, query in enumerate(queries):
        if query[-1] == '?': # 문자로 시작
            cnt = count_by_range(voca[len(query)], query.replace('?','a'), query.replace('?','z'))    
        elif query[0] == '?': # 문자로 끝남
            cnt = count_by_range(voca_reverse[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
        answer.append(cnt)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]	
print(solution(words, queries))
