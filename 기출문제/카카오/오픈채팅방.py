# https://programmers.co.kr/learn/courses/30/lessons/42888
# 카카오 2019 신입 공채
# 풀이) 해쉬

def solution(record):
    d = dict()
    answer = []
    for s in record:
        s = s.split()
        if len(s) == 3:
            d[s[1]] = s[2]

    for s in record:
        s = s.split()
        if s[0] == 'Leave':
            answer.append(d[s[1]] + "님이 나갔습니다.")
        elif s[0] == 'Enter':
            answer.append(d[s[1]] + "님이 들어왔습니다.")

    return answer
        

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))