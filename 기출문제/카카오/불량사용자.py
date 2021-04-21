# https://programmers.co.kr/learn/courses/30/lessons/64064
# 풀이) 순열, 경우의수

from itertools import permutations
def solution(user_id, banned_id):
    n, m = len(user_id), len(banned_id)
    arr = [[] for _ in range(m)] # 각 banned_id에 해당하는 애들 적기!

    case = list(map(list, permutations(user_id, m)))

    for i in range(m):
        for j in range(n):
            ban = list(banned_id[i])
            user = list(user_id[j])
            if len(ban) != len(user):
                continue
            for k in range(len(ban)):
                if ban[k] != '*' and ban[k] != user[k]:
                    break
            else:
                arr[i].append(''.join(user))
    
    res = set()
    for i in range(len(case)):
        visited = set()
        for j in range(m):
            if case[i][j] not in arr[j]:
                break
            if case[i][j] in visited:
                break
            visited.add(case[i][j])

        else:
            res.add(', '.join(sorted(case[i])))

    return len(res)


    

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id = ["fr*d*", "abc1**"]

user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id = ["*rodo", "*rodo", "******"]	

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
# banned_id = ["fr*d*", "*rodo", "******", "******"]	
print(solution(user_id, banned_id))