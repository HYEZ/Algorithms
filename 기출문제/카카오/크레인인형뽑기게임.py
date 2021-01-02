# https://programmers.co.kr/learn/courses/30/lessons/64061
# 카카오 2019 겨울 인턴쉽

# 풀이) 스택

stack = []
def solution(board, moves):
    answer = 0
    stack = [0]

    for j in moves:
        j -= 1
        for i in range(len(board)):
            if board[i][j] != 0:
                if stack[-1] == board[i][j]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][j])
                board[i][j] = 0
                break

    return answer*2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves))