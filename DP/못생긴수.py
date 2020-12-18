# 이것이 코딩테스트다 - 구글 인터뷰

# 오직 2, 3, 5만을 소인수로 가지는 수
# n 번째 못생긴수를 찾는 프로그램
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...

n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])
    