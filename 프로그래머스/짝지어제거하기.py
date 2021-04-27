# https://programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팀스다운
# 풀이) 스택

def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return int(not len(stack))






s = 'baabaa'
s = 'cdcd'
print(solution(s))