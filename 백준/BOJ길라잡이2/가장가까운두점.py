# https://www.acmicpc.net/problem/2261
# 풀이) 분할정복

import math
import sys 
input = sys.stdin.readline

INF = 1e9
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()                

def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2



def solution(start, end):
    if start == end:
        return INF
    else:
        mid = (start + end) // 2
        min_dist = min(solution(start, mid), solution(mid + 1, end))

        candidate = []
        
        for i in range(mid, start-1, -1):
            if (arr[i][0] - arr[mid][0]) ** 2 < min_dist:
                candidate.append(arr[i])
            else:
                break
        
        for i in range(mid+1, end+1):
            if (arr[i][0] - arr[mid][0]) ** 2 < min_dist:
                candidate.append(arr[i])
            else:
                break
        
        candidate.sort(key=lambda x:x[1])

        for i in range(len(candidate) - 1):
            for j in range(i, len(candidate)):
                if (candidate[i][1] - candidate[j][1]) ** 2 < min_dist:
                    dist = distance(candidate[i], candidate[j])
                    min_dist = min(min_dist, dist)
                else:
                    break
        print(min_dist)
        return min_dist


if len(arr) != len(set(arr)):
    print(0)
else:
    print(solution(0, len(arr) - 1))


# def find_nearest(c):
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 dist = distance(arr[i], arr[j])
#                 if dist <= c:
#                     return True
#     return False
# start = 0
# end = 1000000
# res = 0
# while start <= end:
#     mid = (start + end) // 2 # 가장 가까운 점
#     if find_nearest(mid):
#         res = mid
#         end = mid - 1
#     else:
#         start = mid + 1

# print(res)


