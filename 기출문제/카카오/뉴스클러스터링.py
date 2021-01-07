# https://programmers.co.kr/learn/courses/30/lessons/https://programmers.co.kr/learn/courses/30/lessons/17677
# 2018 카카오 신입 공채 1차
# 풀이) 

def solution(str1, str2):
    str1 = make_set(str1.lower())
    str2 = make_set(str2.lower())

    if len(str2) == 0:
        return 65536

    intersection = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            intersection += 1
            str2.pop(str2.index(str1[i]))

    union = len(str1) + len(str2) 
    
    answer = intersection/union * 65536
    return int(answer)

def make_set(s):
    arr = []
    for i in range(1, len(s)):
        if (s[i-1]+s[i]).isalpha():
            arr.append(s[i-1]+s[i])
    return arr

    

# str1 = "FRANCE"
# str2 = 'french'
# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'	
str1 = 	"aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))