def solution (heights):
	answer = []

	# heights : stack
	stk = heights
	tmp = []
	for i in range(len(stk)):
		if len(tmp) > 0: # tmp가 빈 값이 아니면
			# 꺼내서 스택에 넣음
			for i in range(len(tmp)):
				stk.append(tmp.pop())

		cur = stk.pop()
		

		print(heights.pop())


	

	return answer




heights = [6,9,5,7,4]
heights = [3,9,9,3,5,7,2]
heights = [1,5,3,6,7,6,5]
print(solution(heights))

