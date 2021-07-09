import sys
input = sys.stdin.readline

def dfs(idx, sum, flag):
    global cnt, res
    if idx >= n:
        return
    sum += arr[idx]

    if flag:
        if dp[idx] == 0:
            res.append(arr[idx])
            print(arr[idx])
        dp[idx] = 1 
        # print(arr[idx])
    
        
    if sum == s:
        cnt += 1

    dfs(idx + 1, sum - arr[idx], False) # 해당 숫자를 안더했을 경우
    dfs(idx + 1, sum, True) # 해당 숫자를 더했을 경우

n, s = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
cnt = 0
res = []
dfs(0, 0, False)
print((res))
# print(cnt)