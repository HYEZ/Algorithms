# https://programmers.co.kr/learn/courses/30/lessons/76502
# 풀이) 스택

def is_correct(s):
    stack = []
    pair = {'}':'{', ']':'[', ')':'('}

    for i in range(len(s)):
        if s[i] in pair.keys():
            while stack and stack[-1] != pair[s[i]]:
                stack.pop()
            else:
                if stack and stack[-1] == pair[s[i]]:
                    stack.pop()
                else:
                    return False
            
        else:
            stack.append(s[i])

    return not len(stack)
    
    

def solution(s):
    answer = 0

    for i in range(len(s)):
        if is_correct(s):
            answer += 1

        s = s[1:] + s[0]
    
    return answer



s = '[)(]'
print(solution(s))