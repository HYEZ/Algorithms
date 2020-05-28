def solution(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
    	print(i)
    print(citations)
    print(list(map(min, enumerate(citations, start=1))))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]))