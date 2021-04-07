# https://www.acmicpc.net/problem/3090
# 풀이) 이진탐색

import copy

n, t = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 1000000000

def is_possible(diff):
    global tmp
    op_cnt = 0
    tmp = copy.deepcopy(arr)

    for i in range(n-1):
        if tmp[i+1] - tmp[i] > diff:
            op_cnt += tmp[i+1] - (tmp[i] + diff)
            tmp[i+1] = tmp[i] + diff

    for i in range(n-1, 0, -1):
        if tmp[i-1] - tmp[i] > diff:
            op_cnt += tmp[i-1] - (tmp[i] + diff)
            tmp[i-1] = tmp[i] + diff

    if op_cnt <= t:
        return True
    return False


while start <= end:
    mid = (start + end) // 2 # mid : diff max

    if is_possible(mid):
        result = copy.deepcopy(tmp)
        end = mid -1 
    else:
        start = mid + 1
        
print(*result)
        

