def solution (heights):
	answer = []

	# heights : stack
	stk = heights
	tmp = []
	is_cur = False
	cur = 0

	while len(stk) >= 1:

		if is_cur == True and len(tmp) > 0: # tmp가 빈 값이 아니면
			# 꺼내서 스택에 넣음
			while True:
				s = stk.pop()
				if(s > answer[-1]):
					break
				else:
					tmp.append(s)
			print("t", tmp)
			while len(tmp) > 0:
				t = tmp.pop()
				stk.append(t)
			print('s', stk, answer)

		# print(stk)

		cur = stk.pop()

		# cur = stk.pop()
		# print(cur, stk[-1])

		if(cur >= stk[-1]): # 밑에 스택보다 더 크면 => 다른 스택에다가 임시로 넣어둠
			is_cur = True
			print("cur", cur)
			tmp.append(stk.pop())

			
		else: # 다음께 더 크면 답에다 넣고 스택에서 아예 빼버림
			is_cur = False


		answer.append(cur)


	answer.reverse()
	return answer




# heights = [6,9,5,7,4]
heights = [3,9,9,3,5,7,2]
# heights = [1,5,3,6,7,6,5]
print("A", solution(heights))

