# https://programmers.co.kr/learn/courses/30/lessons/64062
# 풀이) 이진탐색


# 방법 2 - 이진탐색
# O(nlongn)
def solution(stones, k): 
    start = 0
    end = 200000000
    
    n = len(stones)
    answer = int(1e9)

    while start <= end: 
        mid = (start + end) // 2 # 건널 수 있는 사람 수

        res = 0
        cnt = 0
        for stone in stones:
            stone = max(stone-mid, 0)
            if stone == 0:
                cnt += 1
            else:
                res = max(cnt, res) # 현재 mid에서 0개수
                cnt = 0   
        res = max(cnt, res)

        if res < k:
            start = mid + 1
        else:
            answer = min(mid, answer)
            end = mid - 1
            
    return answer


# 방법 1 - 구현 (효율성 실패) 
def solution2(stones, k): 
    answer = 0
    n = len(stones)
    
    while True:
        s = -1
        cnt = 1
        for i in range(n):
            s += 1
            if stones[i] == 0:
                cnt += 1 # 건너 뛰는 횟수
                if cnt > k:
                    return answer
                continue
            
            cnt = 1
            stones[i] -= 1

        answer += 1

    return answer
    
    


stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3 # answer: 3
print(solution(stones, k))