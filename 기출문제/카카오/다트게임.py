# https://programmers.co.kr/learn/courses/30/lessons/17682
# 2018 카카오 신입 공채 1차


def solution(dartResult):
    prev = 0
    arr = []
    for i in range(len(dartResult)):
        if dartResult[i] == "*":
            arr[-1] *= 2
            if len(arr) >= 2: 
                arr[-2] *= 2 
            prev += 1
        elif dartResult[i] == "#":
            arr[-1] *= -1
            prev += 1
        elif dartResult[i] == 'S':
            arr.append(int(dartResult[prev:i]))
            prev = i+1
        elif dartResult[i] == 'D':
            arr.append(int(dartResult[prev:i])**2)
            prev = i+1
        elif dartResult[i] == 'T':
            arr.append(int(dartResult[prev:i])**3)
            prev = i+1

    return(sum(arr))

dartResult = "1S*2T*3S"
# dartResult = "1S2D*3T"
# dartResult = "1D2S#10S"
print(solution(dartResult))