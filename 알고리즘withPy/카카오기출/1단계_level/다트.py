import re

def solution(dartResult):
    answer = 0
    charConvert={"S":"**1","D":"**2","T":"**3","#":"*(-1)"}
    # 값을 정규표현식을 이용하여 분리
    # 그룹핑하여 그룹마다 뒤를 스페이스바로 띄어서 변경
    parser=re.sub('([SDT][#*]?)','\g<1> ',dartResult).split()
    print(parser)
    # 다트횟수별로 분할 배열 3개로, 횟수별로 돌면서 계산할거다
    # 시도마다 다트 수식을 저장할 result
    result=[]
    for parse in parser:
        # 계산할 때 charConvert에 있는 경우 키값에 맞는 value값으로 replace 해주고 *은 별도로 처리
        for word in parse:
            #parse 다트던진 것을 계산식으로 replace해주고 다시 저장한다
            #key 값에 해당하는 값이 있으면 해당하는 수식으로 변경해주고 없을 경우 그 문자 그대로 둔다 *은 key값으로 저장안했기 때문에
            parse=parse.replace(word,charConvert.get(word,word))
            # print(parse)
        # *은 처리안해줬기 때문에 맨마지막 부분에 스타상을 선택한사람은 *효과를 적용해주어야한다
        if parse[-1]=="*":
            parse+="2"
            # 두번이상 다트를 쐈으면 그전에 값이 배열로 저장되어있을 것이다.
            if result:
                result[-1]=result[-1]+"*2"
        result.append(parse)
    #     print(parse)
    # print(result)
    for val in result:
        answer+=eval(val)
    return answer


# 예제	dartResult	answer	설명
# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
# 2	1D2S#10S	9	12 + 21 * (-1) + 101
# 3	1D2S0T	3	12 + 21 + 03
# 4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	1T2D3D#	-4	13 + 22 + 32 * (-1)
# 7	1D2S3T*	59	12 + 21 * 2 + 33 * 2