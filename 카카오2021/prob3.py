import math
def cal_fare(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        m = (time-fees[0]) / fees[2]
        m = math.ceil(m)
        return fees[3]*m + fees[1]

def solution(fees, records):
    answer = []
    fare_dic, carin_dic= {}, {}
    
    for record in records:
        t, car, io = record.split()
        t_1, t_2 = t[:2], t[3:]
        t = int(t_1)*60+int(t_2)
        
        if io=="IN":
            carin_dic[car]=t
        # out 일때
        else:
            i=carin_dic[car]
            o=t
            # fare=cal_fare(i,o,fees)
            if fare_dic.get(car):
                fare_dic[car]+=(o-i)
            else:
                fare_dic[car]=(o-i)
            del carin_dic[car]
        print(carin_dic)
        print()
        print(fare_dic)
    out_time=1439
    for k,v in carin_dic.items():
            print(k,out_time-v)
            if fare_dic.get(k):
                fare_dic[k]+=(out_time-v)
            else:
                fare_dic[k]=(out_time-v)
    fare_dic=sorted(fare_dic.items())
    print(fare_dic)
    for k,time in fare_dic:     
        answer.append(cal_fare(time,fees)) 

    return answer


# fees	records	result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
# [1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))