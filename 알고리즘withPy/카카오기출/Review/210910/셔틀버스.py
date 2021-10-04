def solution(n, t, m, timetable):
    answer=""
    bus_time=540
    bus_schedule=[[bus_time,0]]
    
    for _ in range(n-1):
        bus_time+=t
        bus_schedule.append([bus_time,0])
    
    timetable=sorted([int(time[:2])*60+int(time[3:]) for time in timetable])
    
    b=0
    p_cnt=0
    for person in timetable:
        if person<=bus_schedule[b][0]:
            if bus_schedule[b][1]<m:
                p_cnt+=1
                bus_schedule[b][1]+=1
            else:
                if b+1<n:
                    b+=1
                    p_cnt+=1
                    bus_schedule[b][1]+=1
                else:break
        else:
            while True:
                if b+1<n:
                    b+=1
                    if person<=bus_schedule[b][0]:
                        p_cnt+=1
                        bus_schedule[b][1]+=1
                        break
                else:
                    break
        
        result=540
        if bus_schedule[-1][1]<m:
            result=bus_schedule[-1][0]
        else:
            result=timetable[p_cnt-1]-1
        h,min=divmod(result,60)
        answer=str(h).zfill(2)+":"+str(min).zfill(2)
    return answer