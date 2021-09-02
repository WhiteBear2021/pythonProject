import math
# 현재 진도 progress 하루 개발속도 speeds
# 앞의 기능이 배포되지 않으면 뒤의 기능이 완료되어도 앞의 기능이 완료될 때 같이 배포된다. 
def solution(progresses, speeds):
    answer = []
    period = []
    for p,s in zip(progresses,speeds):
        # 걸리는 일수
        time=math.ceil((100-p)/s)
        period.append(time)
    print(period)
    cnt=1
    start_idx=0
    for i in range(0,len(period)-1):
        if period[start_idx]<period[i+1]:
            answer.append(cnt)
            cnt=1
            start_idx=i+1
        else:
            cnt+=1
            
    answer.append(cnt)    
    return answer