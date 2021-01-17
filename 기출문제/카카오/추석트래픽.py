# https://programmers.co.kr/learn/courses/30/lessons/17676
# 카카오 2018 신입 공채 1차
# 풀이) 다시 풀기!!!!!

from datetime import datetime, timedelta

def solution(lines):
    # 1. 시작, 종료 시간 각각 계산 만들기 (시작시간 : 종료시간 - 처리시간(초단위) + 0.001)
    start_times = []
    end_times = []
    for line in lines:
        date, end, t = line.split()
        t = float(t[:-1]) # s 제외시키기
        end_time = datetime.strptime(date + " " + end, '%Y-%m-%d %H:%M:%S.%f')
        start_time = end_time - timedelta(seconds=t) + timedelta(seconds=0.001)
        start_times.append(start_time)
        end_times.append(end_time)

    # 2. 시작, 종료시간 합치기 (처리량이 바뀔때는 새 요청이 들어올 때, 요청이 끝날 때 이므로 두개를 합쳐서 같이 봄!)
    total = start_times + end_times

    sec = timedelta(seconds=1) # 1초
    answer = 0
    
    for start in total:
        tmp = 0
        for i in range(len(end_times)):
            # 해당 로그 기준으로 1초 안에 다른 요청이 처리 되었거나 or 다른 새로운 요청이 들어온경우
            if start <= end_times[i] < start + sec or start <= start_times[i] < start + sec:
                tmp += 1 
            # 아니면 해당 로그 이전에 요청이 들어와서 1초 안에 아직 끝나지 않은 경우
            elif start_times[i] <= start and end_times[i] >= start + sec:
                tmp += 1
        answer = max(answer, tmp)
    
    return answer


lines = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]

print(solution(lines))