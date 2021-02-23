# https://www.acmicpc.net/problem/1931
# 풀이) 그리디
import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

print(arr)

end_time = arr[0][1]
cnt = 1
for i in range(1, n):
    if arr[i][0] >= end_time:
        cnt += 1
        end_time = arr[i][1]
print(cnt)
    

        
            
