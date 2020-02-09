def solution(n, lost, reserve):
    if n < 2 or n > 30:
        return -1
    answer = 0
    chk = [1 for _ in range(n+1)]

    for i in range(len(lost)):
        chk[lost[i]] -= 1

    for i in range(len(reserve)):
        chk[reserve[i]] += 1

    print(chk)

    for i in range(1, n):
        if chk[i] == 0:
            if chk[i-1] == 2:
                chk[i-1] -= 1
                chk[i] = 1
            elif chk[i+1] == 2:
                chk[i] = 1
                chk[i+1] -= 1

    for i in range(1, n+1):
        if chk[i] > 0:
            answer += 1
    return answer
