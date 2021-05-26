# https://programmers.co.kr/learn/courses/30/lessons/77486
# 풀이) 구현, 그래프 - 시간초과..!!


def solution(enroll, referral, seller, amount):
    parent = dict()
    result = dict(zip(enroll, [0]*len(enroll)))
    for i in range(len(referral)):
        parent[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        x = seller[i]
        price = amount[i] *  100
        tmp = dict(zip(enroll, [0]*len(enroll)))

        while True:
            parent_price = int(price * 0.1)
            x_price = price - parent_price
            price = parent_price

            tmp[x] = x_price
            if parent[x] != '-':
                tmp[parent[x]] = price

            x = parent[x]
            if x == '-':
                break
        
        for key in result.keys():
            result[key] += tmp[key]

    return list(result.values())




enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))