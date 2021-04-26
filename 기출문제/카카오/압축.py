# https://programmers.co.kr/learn/courses/30/lessons/17684
# 카카오 2018 신입 공채 3차 코딩테스트 
# 풀이) 투포인터 알고리즘


def solution(msg):
    d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))

    w = msg[0]
    i = 0
    j = 1
    answer = []
    while i < len(msg):

        while j <= len(msg) and msg[i:j] in d.keys():
            j += 1
        
        answer.append(d[msg[i:j-1]])        
        if msg[i:j] not in d.keys():
            d[msg[i:j]] = len(d)+1
        
        i = j - 1
        j = j + 1

    return answer




msg = 'KAKAO'
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
