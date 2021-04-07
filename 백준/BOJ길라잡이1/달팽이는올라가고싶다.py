# https://www.acmicpc.net/problem/2869
# 풀이) 그리디
import math 
a, b, v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))





# res = 0
# while True:
#     res += 1
#     v -= a
#     if v == 0:
#         break
#     v += b
# print(res)
    