# https://programmers.co.kr/learn/courses/30/lessons/60062
# 카카오 2020 신입공채 1차


from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n) # 원형의 길이를 2배로 늘려서 일자형태로 변환함

    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1

    return answer


n = 12
weak = [1, 5, 6, 10]	
dist = [1, 2, 3, 4]	

print(solution(n, weak, dist))