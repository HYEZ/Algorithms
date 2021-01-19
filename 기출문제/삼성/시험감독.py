# https://www.acmicpc.net/problem/13458
# 풀이) 그리디

# 각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.
# 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.
import sys
import math
input = lambda: sys.stdin.readline().strip()

n = int(input()) 
a = list(map(int, input().split()))

b, c = map(int, input().split())

a = [max(0, x - b) for x in a]
res = n

for x in a:
    res += math.ceil(x/c)
    
print(res)