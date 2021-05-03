# https://programmers.co.kr/learn/courses/30/lessons/77484
# 풀이) 해쉬, 구현

def solution(lottos, win_nums):
    zero_cnt = 0
    same_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        elif i in win_nums:
            same_cnt += 1
    
    d = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    return d[same_cnt+zero_cnt], d[same_cnt] 