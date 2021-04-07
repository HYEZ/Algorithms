# https://www.acmicpc.net/problem/2750
# 풀이) 정렬

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in range(n):
    print(arr[i])