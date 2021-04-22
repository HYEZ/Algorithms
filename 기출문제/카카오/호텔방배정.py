# https://programmers.co.kr/learn/courses/30/lessons/64063
# 카카오 2019 겨울 인턴쉽
# 풀이) 해쉬, 이진탐색
import sys
sys.setrecursionlimit(10**9)

from bisect import bisect_left, bisect_right, insort_right

# # 3. 서로소 집합 알고리즘

# def find_parent(parent, x):
#     d

# def solution(k, room_number):
#     # parent = [i for i in range(1, k+1)]
#     parent = [0] * (k+1)
#     customer = [0] * len(room_number)
    

#     for i, n in enumerate(room_number):
#         key = find_parent(parent, n)
#         customer[i] = key

#     return customer


# 2. bisect로 key value 찾기 (효율성 실패)
def solution(k, room_number):
    rooms = []
    customer = [0] * len(room_number)

    def get_key(arr, key):
        left_idx = bisect_left(arr, key)
        right_idx = bisect_right(arr, key)

        if right_idx - left_idx != 0: # 이미 있는 key
            return get_key(arr, key+1)

        return key

    for i, n in enumerate(room_number):
        if n not in rooms:
            key = n
        else:
            key = get_key(rooms, n)
        insort_right(rooms, key)

        customer[i] = key

    return customer



# 3. 해쉬충돌 -> 다음 key value 리니어하게 찾기 (효율성 실패)
def solution1(k, room_number):
    room = [0] * (k+1)
    customer = [0] * len(room_number)

    def get_key(num):
        if room[num] > 0:
            num = get_key(num+1)
        return num

    for i, n in enumerate(room_number):
        key = get_key(n)
        room[key] = 1
        customer[i] = key

    return customer



k = 10
room_number = [1,3,4,1,3,1]	
print(solution(k, room_number))