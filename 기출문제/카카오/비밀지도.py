# https://programmers.co.kr/learn/courses/30/lessons/17681
# 카카오 2018 신입 채용 1차
# 풀이) 비트연산


solution = lambda n, arr1, arr2: (list(map(lambda x, y: ('{:'+str(n)+'b}').format(x|y).replace('1', '#').replace('0', ' '), arr1, arr2)))





n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


print(solution(n, arr1, arr2))