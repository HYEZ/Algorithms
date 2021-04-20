# https://programmers.co.kr/learn/courses/30/lessons/12981
# 풀이) 해시, 집합


def solution(n, words):
    saved = set([words[0]])
    arr = [0] * n
    arr[0] = 1
    
    for i in range(1, len(words)):
        prev = words[i-1]
        now = words[i]
        arr[i%n] += 1
        
        if prev[-1] != now[0] or now in saved:
            return [i%n+1, arr[i%n]]

        saved.add(now)

    return [0, 0]
    

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	
print(solution(n, words))