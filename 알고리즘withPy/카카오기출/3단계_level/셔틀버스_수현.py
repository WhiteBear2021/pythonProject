def solution(n, t, m, timetable):
    answer = ''
    bus = [[(540+t*i),m] for i in range(n)]
    crew = [int(i.split(":")[0])*60+int(i.split(":")[1]) for i in timetable]
    crew.sort()
    b = 0
    print(crew)
    for c in crew:
        print(bus)
        print(c)
        if c<=bus[b][0]:
            if bus[b][1]==0:
                if b + 1 != len(bus):
                    b += 1
                else:
                    break
            bus[b][1]-=1
        else:
            while True:
                if b+1 != len(bus):
                    b+=1
                    if c<=bus[b][0]: 
                        bus[b][1]-=1
                        break
                else:
                    break
            
    total = 0
    print(bus)
    
    if bus[-1][1] != 0:
        answer = bus[-1][0]
    else:
        for i in bus:
            total+=(m-i[1])
        answer = crew[total-1]-1
    if answer == 0:
        answer = "00:00"
    else:
        h, m = divmod(answer, 60)
        answer = str(h).zfill(2)+':'+str(m).zfill(2)
    return answer

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))