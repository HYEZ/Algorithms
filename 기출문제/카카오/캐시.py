# https://programmers.co.kr/learn/courses/30/lessons/17680
# 카카오 2018 신입 공채 1차 코딩테스트
# 풀이) 해쉬, 큐

def solution(cacheSize, cities):
    cache = [0] * cacheSize
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in cache: # hit
            answer += 1
            cache.pop(cache.index(city))
        else: # miss
            answer += 5

        cache.append(city)
        
        if len(cache) > cacheSize:
            cache.pop(0)

    return answer
        



cacheSize, cities = 2, ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))