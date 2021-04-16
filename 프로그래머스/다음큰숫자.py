# https://programmers.co.kr/learn/courses/30/lessons/12911
# 풀이) 그리디


def len_one(n):
        binary = '{0:b}'.format(n)
        return sum(list(map(int, list(binary))))
    
def solution(n):
    n_one = len_one(n)
    m = n + 1
    while True:
        m_one = len_one(m)
        if n_one == m_one:
            return m
        m += 1


n = 78
print(solution(n))