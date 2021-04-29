# https://programmers.co.kr/learn/courses/30/lessons/12941
# 풀이) 그리디, 정렬

def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
 
    return answer


A, B = [1, 4, 2], [5, 4, 4]
print(solution(A, B))