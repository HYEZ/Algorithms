# https://programmers.co.kr/learn/courses/30/lessons/17686
# 카카오 2018 신입 공채 3차 코딩테스트
# 풀이) 정렬

def solution(files):
    arr = []
    for file in files:
        start = 0
        while not file[start].isdigit():
            start += 1
        
        end = start
        while end < len(file) and not file[end].isalpha():
            end += 1

        if end != len(file):
            end -= 1

        head = file[:start].lower()
        number = int(file[start:end])

        arr.append((head, number, file))

    arr.sort(key=lambda x: (x[0], x[1]))
    return [x[2] for x in arr]
        
            
            






files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "F-15"]
print(solution(files))