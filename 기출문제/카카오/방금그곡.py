# https://programmers.co.kr/learn/courses/30/lessons/17683
# 카카오 2018 신입 공채 3차 코딩테스트
# 풀이) 해쉬, 구현

def str_to_int(time):
    h, m = time.split(':')
    return int(h) * 3600 + int(m) * 60
            
def time_to_minute(time):
    h = time // 3600
    time = time % 3600
    m = time // 60
    return m + h*60

def song_to_alpha(song):
    song = list(song) 
    d = dict(zip(['A#', 'C#', 'D#', 'F#', 'G#', 'E#'], ['H', 'I', 'J', 'K', 'L', 'M']))
    for i in range(len(song)):
        if song[i] == '#':
            song[i-1] += '#'
            song[i-1] = d[song[i-1]]
            song[i] = ''

    return ''.join(song)


def get_full_song(song, time):
    song = song_to_alpha(song)
    
    n = len(song)
    k = 1440 // n
    
    song *= k
    return song[:time]


def solution(m, musicinfos):
    m = song_to_alpha(m)
    n = len(musicinfos)
    max_time = 0
    answer = '(None)'

    for i in range(n):
        start, end, title, song = musicinfos[i].split(',')
        time = str_to_int(end) - str_to_int(start)
        time = time_to_minute(time)
        song = get_full_song(song, time)
        
        if m in song:
            if time > max_time:
                max_time = time
                answer = title
            
    return answer


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	


print(solution(m, musicinfos))
	