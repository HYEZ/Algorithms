# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    collected = []  

    for i, num in enumerate(number):

        # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1

        if k == 0:
            collected += list(number[i:])
            break
        
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected # 같은 숫자 여러번 반복일때 k 가 남을 수도 있어서 그거 방지함

    return ''.join(collected)


number = "1924"
k = 2

# number = "1231234"
# k = 3

number= "99991"
k = 2
print(solution(number, k))