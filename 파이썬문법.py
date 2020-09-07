
# 리스트 컴프리헨션
arr = [i*i for i in range(20) if i % 2 == 1]

# 2차원 리스트 초기화
n = 4
m = 5
arr = [[0]*m for _ in range(n)] # NxM

# removeAll 구현
a = [1, 2, 3, 4, 5, 6, 7]
remove_set = {3, 5}
arr = [i for i in a if i not in remove_set]

print(arr)

# 문자열
# 문자열은 특정원소의 값을 바꾸는 것은 안된다!
s = "hello's \"python"
print(s)

# 딕셔너리 : O(1)
d = dict()
d['사과'] = 'apple'
key_list = list(d.keys())
value_list = list(d.values())
if '사과' in d:
	print('사과가 있습네다')

# 집합 : O(1) => 단순히 값을 찾을때 유용, 리스트나 튜플은 O(n)
a = {1, 2, 3}
b = {2, 5}
print(1 in a)
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
a.add(5)
a.update([5, 6]) # 새로운 원소 여러개 추가
a.remove(3)
print(a)

print({1, 2} in {1, 2, 3})

a = 11
b = "Success" if a > 10 else "Fail" # 한줄일때만 가능
print(b)

# 람다(익명함수)
def add(a,b):
	return a + b
print(add(1, 2))
print((lambda a, b: a + b)(1, 2))
a = lambda a,b:a+b
print(a(1, 2))

a = [(1, 2), (3, 4)]
a = sorted(a, key = lambda x : x[1], reverse=True )
print(a)

a = [1, 2, 3]
b = [1, 2, 3]
c = map(lambda a, b: a + b, a, b)
print(list(c))

# 표준 라이브러리
# itertools
# heapq
# bisect
# collections : Counter, deque

# 순열, 조합
from itertools import permutations, combinations
data = [1, 2, 3, 6]
a = list(permutations(data, 3))
b = list(combinations(data, 3))
print(a)
print()
print(b)

# 중복순열, 중복조합
from itertools import product, combinations_with_replacement
a = list(product(data, repeat=2))
b = list(combinations_with_replacement(data, 2))
print(a)
print(b)

# heapq

# bisect

# deque
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)

# counter
from collections import Counter

counter = Counter(['red', 'blue', 'red'])
print(dict(counter))
print(counter['blue'])

# math
import math
print(math.factorial(5))
print(math.gcd(21, 3)) # 최대공약수

# 입력
# a, b, c, d, e = map(int, input().split()) # 5개의 정수 입력받기
# n = int(input()) # 데이터의 개수
# a = list(map(int, input().split())) # 데이터 입력받기
# # print(a)

# # 2차원 배열 입력
# n = int(input())
# m = int(input())
# arr = []
# for i in range(n):
# 	arr.append(list(map(int, input().split())))


# # 문자열 빠르게 입력받기
# import sys 
# data = sys.stdin.readline.rstrip()

