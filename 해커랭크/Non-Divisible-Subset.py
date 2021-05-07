# https://www.hackerrank.com/challenges/non-divisible-subset/problem
# 풀이) 그리디


def nonDivisibleSubset(k, s):
    div = [x%k for x in s] 
    result = 0 # 부분집합 크기

    for i in range(1, k//2+1): # (1, k-1), (2, k-2), ..., 나머지가 0~k-1까지 있으므로 (두 수의 나머지의 합이 k가 아니면 됨)
        if i != k-i: # 나머지가 k//2가 아닌 경우 i랑 k-i 중 더 많은쪽 포함
            result += max(div.count(i), div.count(k-i))
        else: # 나머지가 k//2인경우
            result += int(bool(div.count(i)))
    
    print(div)
    result += int(bool(div.count(0))) # 나머지가 0인 경우
    return result

k = 3
s = [1, 7, 2, 4]

k = 4 
s = [1, 7, 2, 4]

# k = 7
# s = list(map(int, input().split()))
print(nonDivisibleSubset(k, s))
