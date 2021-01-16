# https://programmers.co.kr/learn/courses/30/lessons/17687
# 카카오 2018 신입 공채 3차
# 풀이) n진법구하기, 구현

def solution(n, t, m, p):
    i = 1
    number = ['0']
    while True:
        number += change_number(i, n)
        i += 1
        if len(number) >= m * t:
            break

    answer = []
    for i in range(p-1, m*t, m):
        answer.append(number[i])
    
    return ''.join(answer)


def change_number(number, n):
    answer = ''
    chars = '0123456789ABCDEF'
    while number:
        remain = chars[number % n]
        number = number // n
        answer = str(remain) + answer
    return list(answer)


n, t, m, p = 2,4,2,1
print(solution(n, t, m, p))