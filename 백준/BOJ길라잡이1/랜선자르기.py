# https://www.acmicpc.net/problem/1654
# 풀이) Binary Search

k, n = map(int, input().split()) # 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
arr = []
for _ in range(k):
    arr.append(int(input()))

arr.sort()

start = 0 
end = max(arr)
res = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    if mid == 0:
        res = max(mid, res)
        break
    for i in range(k):
        total += arr[i] // mid
    if total < n:
        end = mid - 1
    else:
        res = max(mid, res)
        start = mid + 1

print(res)


