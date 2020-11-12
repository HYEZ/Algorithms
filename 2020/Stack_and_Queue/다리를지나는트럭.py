# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_weight = truck_weights[0]
    truck_weights = deque(truck_weights)
    q = deque([truck_weights.popleft()])
    t = 0
    while q:
        t += 1
        if len(q) == bridge_length:
            total_weight -= q.popleft()

        if not truck_weights:
            break

        if total_weight + truck_weights[0] <= weight:
            p = truck_weights.popleft()
            total_weight += p
            q.append(p)
        else:
            q.append(0)

    return t + bridge_length



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]	

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]	

print(solution(bridge_length, weight, truck_weights))