# https://programmers.co.kr/learn/courses/30/lessons/77485
# 풀이) 구현

    
def rotate(x1, y1, x2, y2):
    global arr

    res = int(1e9)
    now = arr[x1][y1]
    for i in range(y1+1, y2+1):
        res = min(now, res)
        arr[x1][i], now = now, arr[x1][i]
        
    for i in range(x1+1, x2+1):
        res = min(now, res)
        arr[i][y2], now = now, arr[i][y2]
        
    for i in range(y2-1, y1-1, -1):
        res = min(now, res)
        arr[x2][i], now = now, arr[x2][i]
    
    for i in range(x2-1, x1-1, -1):
        res = min(now, res)
        arr[i][y1], now = now, arr[i][y1]

    
    return res


def solution(rows, columns, queries):
    global arr
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
            
    for x1, y1, x2, y2 in queries:
        res = rotate(x1-1, y1-1, x2-1, y2-1)
        answer.append(res)
        
    return answer   


rows, columns, queries = 6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))