# https://programmers.co.kr/learn/courses/30/lessons/72410
# 카카오 2021 신입공채
# 풀이) 구현, 정규식

import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id) # 2단계
    new_id = re.sub('[.]{1,}', '.', new_id) # 3단계
    new_id = re.sub('^[.]', '', new_id) # 4단계
    new_id = re.sub('[.]$', '', new_id)

    if new_id == '': # 5단계
        new_id = 'a'

    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        new_id = re.sub('[.]$', '', new_id)

    s = new_id[-1] # 7단계 
    while len(new_id) <= 2:
        new_id = new_id + s     
    
    return new_id 
    

id = "...!@BaT#*..y.abcdefghijklm"	
print(solution(id))
