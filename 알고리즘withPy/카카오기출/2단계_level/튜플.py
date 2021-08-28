import re
def solution(s):
    answer = []
    # 이거 아직 안됨. s=re.sub("([0-9]+[,0-9]*)","\g<1>",s)
    # print(s)
    p=re.compile("[0-9]+[,0-9]*")    
    s=p.findall(s)
    # print(s)
    s.sort(key=lambda x:len(x))
    # print(s)
    c=0
    for i in range(len(s)):
        v_list=s[i].split(",")
        # print(v_list)
        if i==0:
            answer.append(int(v_list[i]))
        else:
            for v in v_list:
                if int(v) not in answer:
                    answer.append(int(v))
                    break
    return answer