# https://programmers.co.kr/learn/courses/30/lessons/60057
# 2020 카카오 블라인드채용

def solution(s):
    answer = int(1e9)
    for i in range(1, len(s)):
        # i 단위로 자르기
        
        for j in range(1, i+1):
            print(i, j)
            for k in range(j, len(s), i):
                
                print(s[j:k], end='_')
            print()

        
            

s = "aabbaccc"	
print(solution(s))