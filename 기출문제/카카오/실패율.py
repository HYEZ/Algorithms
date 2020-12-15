# https://programmers.co.kr/learn/courses/30/lessons/42889
# 2019 카카오 신입공채 1차

# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

def solution(N, stages):
    s = []

    for i in range(1, N+1):
        a = sum([x >= i for x in stages]) # 스테이지에 도달한 플레이어 수
        b = sum([x == i for x in stages]) # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 
        if a == 0:
            x = 0
        else:
            x = b/a
        s.append((x, -i))

    s.sort(reverse=True)
    return [-x[1] for x in s]

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

n = 4
stages = [4,4,4,4,4]	
print(solution(n, stages))