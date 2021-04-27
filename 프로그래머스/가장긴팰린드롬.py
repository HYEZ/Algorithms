# https://programmers.co.kr/learn/courses/30/lessons/12904
# 풀이) 완전탐색

def solution(s):
    answer = 1

    for i in range(len(s)-1):
        for j in range(i+1, len(s)+1):
            now = s[i:j]
            if len(now) > answer:
                if now == now[::-1]:
                    answer = len(now)

    return answer


s = 'abacde'
print(solution(s))