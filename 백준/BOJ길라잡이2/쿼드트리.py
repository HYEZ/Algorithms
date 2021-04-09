# https://www.acmicpc.net/problem/1992
# 풀이) 재귀, 스택

n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]

def compress(arr):
    n = len(arr)
    chk_same = sum([sum(arr[i]) for i in range(n)])
    if chk_same == n*n or chk_same == 0:
        return str(arr[0][0])
    
    if n == 2:
        s = [str(arr[j][i]) for j in range(n) for i in range(n)]
        return '(' + ''.join(s) + ')'
    else:
        tmp1 = [[arr[i][j] for j in range(0, n//2)] for i in range(0, n//2)]
        tmp2 = [[arr[i][j] for j in range(n//2, n)] for i in range(0, n//2)]
        tmp3 = [[arr[i][j] for j in range(0, n//2)] for i in range(n//2, n)]
        tmp4 = [[arr[i][j] for j in range(n//2, n)] for i in range(n//2, n)]
        return '(' + compress(tmp1) + compress(tmp2) + compress(tmp3) + compress(tmp4) + ')'
        

res = compress(arr)      
print(res)
