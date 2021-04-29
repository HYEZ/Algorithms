# https://programmers.co.kr/learn/courses/30/lessons/12949
# 풀이) zip

# 풀코딩
def solution(A, B):
    return [[(sum(a*b for a, b in zip(A_row, B_col))) for B_col in zip(*B)] for A_row in A]

# 넘파이 사용
# import numpy as np
# def solution_np(arr1, arr2):
    # return np.dot(arr1, arr2).tolist()


arr1, arr2 = [[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]
print(solution(arr1, arr2))