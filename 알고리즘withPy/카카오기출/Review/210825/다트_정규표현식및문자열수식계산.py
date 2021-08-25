# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T

# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
import re
charConverter={"S":"**1","D":"**2","T":"**3",
               "#":"*(-1)"}
def solution(dartResult):
    answer = 0
    # step1. 다트별로 3번 분리해서 배열에 저장해준다.(정규표현식 이용)
    dartResult=re.sub("([SDT][*#]?)","\g<1> ",dartResult)
    print(dartResult)
    # 띄어쓰기를 기준으로 세번을 나눈 결과를 배열로 만들어 준다
    dartResult=dartResult.split()
    print(dartResult)
    # 다트별로 답의 목록을 넣을 것이다. result
    result=[]
    # for문으로 다트 한번씩 체크할 수 있다.
    for dart in dartResult:
        # 다트의 내용을 하나씩 확인 문자열(숫자, SDT, *#)
        for s in dart:
            # 딕셔너리에 속한 문자열 수식으로 변경해준다 나중에 eval()함수를 이용할 것이다. 
            dart=dart.replace(s,charConverter.get(s,s))
            if s=="*":
                dart+="2"
                if result:
                    result[-1]+="*2"
        result.append(dart)
    print(result)
    for r in result:
        val=eval(r)
        answer+=val
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))