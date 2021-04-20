# https://programmers.co.kr/learn/courses/30/lessons/70129
# 풀이) 구현

# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수
def solution(s):
    def convert(s):
        s = s.replace('0', '')
        s = format(len(s), 'b')
        return s

    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = convert(s)
        
    return answer



s = '1111111'
print(solution(s))