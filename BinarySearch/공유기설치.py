# https://www.acmicpc.net/problem/2110

# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.


n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

answer = 0
while start <= end:
    mid = (start + end) // 2  # mid는 가장 인접한 거리의 최대값을 의미
    pre_c = house[0] # 공유기간 거리를 계산하기 위해서 이전 공유기 위치 (초기값은 첫번째 집) 
    cnt = 1 # 설치한 공유기 개수. 초기값을 1로 설정 (우선 첫번째 집에 설치한걸로 침)
    min_value = 1000000001 # 최소값 초기화 (가장 인접한 거리)

    for i in range(1, len(house)):
        if house[i] - pre_c >= mid: # 공유기간 거리가 mid보다 크거나 같은경우에만 공유기 설치함 (mid가 가장 인접한 거리이므로)
            cnt += 1 # 공유기 설치
            min_value = min(min_value, house[i]-pre_c) # 최소값 업데이트
            pre_c = house[i] # 이전 공유기 위치 바꿔줌

    if cnt < c: # 설치한 공유기가 c보다 작으면 => 더 설치해줘야함 => mid 줄여주기
        end = mid - 1
    else: # 설치한 공유기가 c보다 크거나 같으면 => mid를 늘려줌, 즉, 최대값 늘려줌
        answer = max(answer, min_value) # 답을 위에서 구한 가장인접한거리(=공유기간 최소값)로 바꿔줌
        start = mid + 1 

print(answer)


