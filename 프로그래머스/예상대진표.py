# https://programmers.co.kr/learn/courses/30/lessons/12985
# 풀이) 재귀

def recursion(arr, a, b, cnt):
    if len(arr) == 0 or len(arr) == 1:
        return cnt

    new_arr = []
    for i in range(0, len(arr), 2):
        if (arr[i] == a and arr[i+1] ==b) or (arr[i] == b and arr[i+1] == a):
            return cnt
        if arr[i] == a or arr[i+1] == a:
            new_arr.append(a)
        elif arr[i] == b or arr[i+1] == b:
            new_arr.append(b)
        else:
            new_arr.append(arr[i])
    
    return recursion(new_arr, a, b, cnt+1)
        

def solution(n, a, b):
    arr = range(1, n+1)
    return recursion(arr, a, b, 1) 


n, a, b = 8, 4, 7
print(solution(n, a, b))