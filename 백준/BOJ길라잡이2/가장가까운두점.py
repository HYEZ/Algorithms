# https://www.acmicpc.net/problem/2261
# 풀이) 분할정복.. 매우 어려움

import math
import sys 
input = sys.stdin.readline

INF = 1e9
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

# x로 정렬 
arr.sort()                

def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def solution(start, end):
    if start == end: # 분할 못하는경우~
        return INF # 거리를 계산할수 없으므로 무한대 리턴~
    else:
        mid = (start + end) // 2
        min_dist = min(solution(start, mid), solution(mid + 1, end)) # 반으로 분할, 왼쪽 오른쪽중 최소 구하기

        candidate = []

        # x부터 보자
        # m을 기준으로 왼쪽 탐색, m의 x좌표와의 거리가 min_dist 미만인 점들 찾기
        for i in range(mid, start-1, -1):
            if (arr[i][0] - arr[mid][0]) ** 2 < min_dist:
                candidate.append(arr[i])
            else:
                break
        
        # m을 기준으로 오른쪽 탐색, m의 x좌표와의 거리가 min_dist 미만인 점들 찾기
        for i in range(mid+1, end+1):
            if (arr[i][0] - arr[mid][0]) ** 2 < min_dist:
                candidate.append(arr[i])
            else:
                break
        

        # 후보들을 y축으로 정렬 (x 좌표는 비슷한점 모았으므로 y좌표가 가까운점 비교하기 위해!)
        candidate.sort(key=lambda x:x[1])

        # y에 대해서 보기
        for i in range(len(candidate) - 1):
            for j in range(i+1, len(candidate)):
                if (candidate[i][1] - candidate[j][1]) ** 2 < min_dist:
                    dist = distance(candidate[i], candidate[j])
                    min_dist = min(min_dist, dist)
                else:
                    break

        return min_dist # 왼쪽애들중 최소, 오른쪽애들중 최소, mid를 걸쳐서 생성된 영역의 최소. 이 3개중 최소임 


if len(arr) != len(set(arr)):
    print(0)
else:
    print(solution(0, len(arr) - 1))
