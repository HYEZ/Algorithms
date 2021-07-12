# https://www.acmicpc.net/problem/14499
# 삼성 SW 역량 테스트
# 풀이) 구현


# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

# 칸에 0 => 주사위 바닥면에 쓰여있는 숫자가 칸에 복사됨
# 칸에 0이 아님 => 칸에 쓰여있는 수가 주사위 바닥면, 칸은 0

n, m, x, y, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

op = list(map(lambda x: int(x)-1, input().split())) # 동쪽은 0, 서쪽은 1, 북쪽은 2, 남쪽은 3

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

box = [0, 0, 0, 0, 0, 0, 0] # 주사위 (-, 1, 2, 3, 4, 5, 6)

def rotate(box, d):
    if d == 0: # 동쪽 3
        # 2, 5는 그대로
        box = [0, box[4], box[2], box[1], box[6], box[5], box[3]]
        
    elif d == 1: # 서쪽 4
        # 2, 5는 그대로
        box = [0, box[3], box[2], box[6], box[1], box[5], box[4]]
        pass
    elif d == 2: # 북쪽 2
        # 3, 4는 그대로
        box = [0, box[5], box[1], box[3], box[4], box[6], box[2]]
        pass
    else: # 남쪽 5
        # 3, 4는 그대로
        box = [0, box[2], box[6], box[3], box[4], box[1], box[5]]
        pass
    
    return box



for d in op:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= 0 and ny >= 0 and nx < n and ny < m:
        box = rotate(box, d)
        top = box[1]
        bottom = box[6]
        now = arr[nx][ny]
        if now == 0:
            arr[nx][ny] = bottom
        else:
            box[6] = arr[nx][ny]
            arr[nx][ny] = 0

        print(top)


        x = nx
        y = ny