# https://www.acmicpc.net/problem/10827
# 풀이) decimal (부동소수점 연산)

from decimal import *

getcontext().prec = 1100
a, b = map(Decimal, input().split())

answer = ("{:f}".format(pow(a, b)))
print(answer)