# 고민1 : 어떻게 주어진 문자열을 나눌 것인가
# -정규표현식을 이용하여 {}안에있는 숫자+알파값들을 배열로 묶어줄것이다. p.findall("정규표현식이용")
# 접근1 : , 을 기준으로 split을 이용하여 문자열을 배열로 저장하기
# 접근2 : 저장된 2차원 배열의 길이를 기준으로 sort
# answer이 비어있으면 값을 넣고, 비어있지않으면 answer에 있는 값들이 아닐 경우에만 정답을 추가해주가
s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
s="{{1,2,3},{2,1},{1,2,4,3},{2}}"
# 결과값: [2, 1, 3, 4]
import re
def solution(s):
    answer = []
    p=re.compile("[0-9]+[0-9,]*")
    s=p.findall(s)
    # print(s)
    s.sort(key=lambda x:len(x))
    for v in s:
        val=v.split(",")
        print(val)
        for i in val:
            print(i,answer)
            if answer:
                if int(i) not in answer:
                    answer.append(int(i))
                    break
            else:
                answer.append(int(i))
                break
        print(answer)
    return answer

print(solution(s))