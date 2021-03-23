# https://programmers.co.kr/learn/courses/30/lessons/72414
# 카카오 2021 공채
# 풀이) DP


# 공익광고 들어갈 시작시간 리턴
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    dp = [0] * (play_time + 1)

    
    for log in logs:
        start, end = log.split('-')
        start, end = str_to_int(start), str_to_int(end)
        dp[start] += 1
        dp[end] -= 1
    
    # 구간별 시청자수 기록
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]  

    # 모든 시청자 수 누적
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]    
    
    # 누적된 시청자수를 바탕으로 가장 시청자수가 많은 구간 탐색
    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                max_time = i - adv_time + 1

        else:
            if most_view < dp[i]:
                most_view = dp[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
   
            
def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s




    

    


play_time,	adv_time,	logs = "02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))