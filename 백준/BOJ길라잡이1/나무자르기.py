# https://www.acmicpc.net/problem/2805
# 풀이) 이진탐색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

start = 0
end = arr[-1]
res = 0
while start <= end:
    mid = (start + end) // 2
    tree = sum([i-mid if mid < i else 0 for i in arr])
  
    if tree < m:
        end = mid - 1
        
    else:
        res = max(mid, res)
        start = mid + 1

print(res)