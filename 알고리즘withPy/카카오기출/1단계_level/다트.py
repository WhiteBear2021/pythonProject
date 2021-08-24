def solution(dartResult):
    answer = 0
#     값을 저장하기 3개 배열에
    num_list=[[] for _ in range(3)]
#     입력받은 문자를 하나씩 for문을 돈다
    idx=-1
    result=0
    for s in dartResult:
       if s.isdigit():
           idx+=1
           num_list[idx].append(int(s))
       else:
           num_list[idx].append(s)
    print(num_list)
    val=0
    # chk 값이 1이면 # 2이면 *
    chk=3
    pre_val=0
    for data in num_list:
        pre_val=val
        # 3번째 값 *, # 값이 없을 경우
        if len(data)==2:
            val=data[0]
            if data[1]=="D":
                val**=2
            elif data[1]=="T":
                val**=3   
            chk=3
        # 3번째 값 * # 값이 있을 경우 
        else:
            val=data[0]
            if data[1]=="D":
                val**=2
            elif data[1]=="T":
                val**=3   
            if data[2]=="*":
                val*=2
                if chk==1:
                    answer-=3*pre_val
                if chk==2:
                    answer+=2*pre_val
            elif data[2]=="#":
                val*=-1
        answer+=val        
            
    return answer

print(solution('1S2D*3T'))