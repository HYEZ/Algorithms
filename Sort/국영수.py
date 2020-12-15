# https://www.acmicpc.net/problem/10825

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

n = int(input())
students = []

for _ in range(n):
    student = input().split()
    students.append((-int(student[1]), int(student[2]), -int(student[3]), student[0]))

students.sort()

for a, b, c, d in students:
    print(d)