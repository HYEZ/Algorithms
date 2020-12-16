# 이것이 코딩테스트다 (zoho 인터뷰)

from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
arr = list(map(int, input().split()))


# arr = [1, 2, 4, 4, 8]
# x = 4
res = bisect_right(arr, x) - bisect_left(arr, x)
if res == 0:
    print(-1)
else:
    print(res)
