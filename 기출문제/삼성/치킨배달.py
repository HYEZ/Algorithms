# https://www.acmicpc.net/problem/15686
# 삼성전자 SW 역량테스트

from itertools import combinations

n, m = map(int, input().split())
city = []
for i in range(n):
    row = list(map(int, input().split()))
    city.append(row)

store = []
home = []
answer = 0

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            store.append((i, j))
        elif city[i][j] == 1:
            home.append((i, j))


stores = list(combinations(store, m))

def get_distance(store):
    answer = 0
    for i, j in home:
        d = 1e9
        for x, y in store:
            d = min(d, abs((x+1)-(i+1)) + abs((y+1)-(j+1)))
        answer += d
    return answer

answer = 1e9
for s in stores:
    answer = min(answer, get_distance(s))


print(answer)          

