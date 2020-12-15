# https://www.acmicpc.net/problem/18310
# 2019 소프트웨어 마에스트로 입학 테스트
# 풀이) 정렬

# 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다. 

n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(len(house)-1) // 2])


