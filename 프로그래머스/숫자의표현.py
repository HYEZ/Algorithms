# https://programmers.co.kr/learn/courses/30/lessons/12924
# 풀이) 완전탐색

def solution(n): # 효율성 실패
    answer = 0
    for i in range(1, n+1):
        res = 0
        for j in range(i, n+1):
            res += j
            if res > n:
                break
            elif res == n:
                answer += 1
                break
    return answer

        

n = 15
print(solution(n))