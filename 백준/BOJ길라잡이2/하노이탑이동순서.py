# https://www.acmicpc.net/problem/11729
# 풀이) 재귀

n = int(input())
def hanoi(n, start, dist, assist):
    global res
    if n == 1:
        res.append([start, dist])
    else:
        hanoi(n-1, start, assist, dist)
        res.append([start, dist])
        hanoi(n-1, assist, dist, start)

res = []
hanoi(n, 1, 3, 2)
print(len(res))
for x, y in res:
    print(x, y)
