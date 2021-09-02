a="CC#BCC#BCC#BCC#B"
b=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# 	"FOO"
import re
import datetime as dt
def chng_hash(m):
    return m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    

def solution(m, musicinfos):
    answer = ''
    max_play=0
    m=chng_hash(m)
    for info in musicinfos:
        music=info.split(",")
        start=dt.datetime.strptime(music[0],"%H:%M")
        end=dt.datetime.strptime(music[1],"%H:%M")
        gap=(end-start)
        gap=gap.seconds//60
        # print(gap)
        
        melody=re.sub("([A-Za-z])","\g<1> ",chng_hash(music[3])).split()
        play_mel=""
        for t in range(gap):
            idx=t%len(melody)
            play_mel+=melody[idx]
        # print(play_mel)
        # print(music)
        print(melody)
        
        if m in play_mel:
            if gap>max_play:
                max_play=gap
                answer=music[2]
    if answer=="":
        answer="(None)"
    return answer
    
print(solution(a,b))