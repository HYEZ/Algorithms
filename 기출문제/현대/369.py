# 2021 현대 엔지비 softeer OT
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
res = 0
for i in range(1, n+1):
    c = Counter(list(str(i)))
    if '3' in c.keys():
        res += c['3']
    if '6' in c.keys():
        res += c['6']
    if '9' in c.keys():
        res += c['9']
        
print(res)



