def solution(n, t, m, timetable):
    answer = ''
    shuttle_time=540
    shuttle_schedule=[[shuttle_time,0]]
    for _ in range(n-1):
        shuttle_time+=t
        shuttle_schedule.append([shuttle_time,0]) 
    wait_list=[]
    for time in timetable:
        time=time.split(":")
        min=int(time[0])*60+int(time[1])
        wait_list.append(min)        
    wait_list.sort()
    # print(shuttle_schedule)
    # print(wait_list)
    num=0
    cnt=0
    for person in wait_list:
        print(m)
        if person<=shuttle_schedule[num][0]:
            if shuttle_schedule[num][1]>=m:
                if num==n-1:
                    break
                else:
                    num+=1
                    shuttle_schedule[num][1]+=1
                    cnt+=1
            else:
                shuttle_schedule[num][1]+=1
                cnt+=1    
        else:
            while True:
                if num==n-1:
                    break
                else:
                    num+=1
                    if person<=shuttle_schedule[num][0]:
                        shuttle_schedule[num][1]+=1
                        cnt+=1
                        break
    print(wait_list)
    print(shuttle_schedule[-1][1],m)
    if shuttle_schedule[-1][1]<m:
        an=shuttle_schedule[-1][0]
    else:
        an=wait_list[cnt-1]-1
    h,m=divmod(an,60)
    answer=str(h).zfill(2)+":"+str(m).zfill(2)
                    
    return answer


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# n	t	m	timetable	answer
# 1	1	5	["08:00", "08:01", "08:02", "08:03"]	"09:00"
# 2	10	2	["09:10", "09:09", "08:00"]	"09:09"
# 2	1	2	["09:00", "09:00", "09:00", "09:00"]	"08:59"
# 1	1	5	["00:01", "00:01", "00:01", "00:01", "00:01"]	"00:00"
# 1	1	1	["23:59"]	"09:00"
# 10	60	45	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	"18:00"