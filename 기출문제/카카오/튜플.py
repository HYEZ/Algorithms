# https://programmers.co.kr/learn/courses/30/lessons/64065
# 카카오 2019 겨울 인턴십 
# 풀이) 집합, 리스트

def solution(s):
    s = s.split('},{')
    s = [x.split(',') for x in s]
    for i in range(len(s)):
        s[i] = [(x.replace('}','').replace('{', '').replace(',','')) for x in s[i]]
    s.sort(key=lambda x: len(x))
    
    answer = []
    prev = set()
    for x in s:
        x = set(x)
        answer.append(int((x - prev).pop()))
        prev = x
    return answer
        
        


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	
s = '{{20,111},{111}}'
print(solution(s))