def change_to_seconds(t):
    h,m,s=t.split(":")
    total_seconds=int(h)*3600+int(m)*60+int(s)
    return total_seconds

def solution(play_time, adv_time, logs):
    answer = ''
    play_time=change_to_seconds(play_time)
    # print(play_time)
    adv_time=change_to_seconds(adv_time)
    # print(adv_time)
    play_sum=[0]*(play_time+1)
    for log in logs:
        start,end=log.split("-")
        # print(start,end)
        start=change_to_seconds(start)
        end=change_to_seconds(end)
        play_sum[start]+=1
        play_sum[end]-=1
    for i in range(1,len(play_sum)):
        play_sum[i]+=play_sum[i-1]
    print(play_sum)
    max_sum=sum(play_sum[:adv_time])
    cur_sum=max_sum
    adv_start=0
    for t in range(1,len(play_sum)-adv_time):
        cur_sum+=-play_sum[t-1]+play_sum[t+adv_time]
        if cur_sum>max_sum:
            adv_start=t
    print(max_sum,adv_start)
 
    answer='%02d:%02d:%02d'%(adv_start/3600,adv_start/60%60,adv_start%60)
    return answer


print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# play_time	adv_time	logs	result
# "02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
# "99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
# "50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	"00:00:00"