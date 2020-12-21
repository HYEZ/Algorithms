# https://www.acmicpc.net/problem/18353

# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다.
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 
# 그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.



n = int(input())
arr = list(map(int, input().split()))


arr.reverse()
dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
