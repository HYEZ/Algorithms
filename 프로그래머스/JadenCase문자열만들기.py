# https://programmers.co.kr/learn/courses/30/lessons/12951
# 풀이) 문자열

def solution(s):
    s = s.lower()
    answer = ''
    for x in s.split(' '):
        answer += x.capitalize() + ' '
    
    return answer[:-1]
