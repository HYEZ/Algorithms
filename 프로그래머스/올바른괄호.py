# https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3
# 풀이) 스택

def solution(s):
    s = list(s)
    stack = [s[0]]
    for i in range(1, len(s)):
        
        if len(stack) > 0 and stack[-1] == '(' and s[i] == ')':
            stack.pop()
        else:
            stack.append(s[i])

    return not len(stack)

s = "()()"	
print(solution(s))