# https://programmers.co.kr/learn/courses/30/lessons/49993
# 풀이) 정규식

import re 
def solution(skill, skill_trees):
    skill_trees = [re.sub(f'[^{skill}]', '',  x) for x in skill_trees]
    cnt = 0
    for s in skill_trees:
        if skill[:len(s)] == s:
            cnt += 1
    return cnt


    

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	
print(solution(skill, skill_trees))