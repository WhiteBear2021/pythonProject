def solution(clothes):
    answer = 1
    clothes_dict={}
    for cloth in clothes:
        kind=cloth[1]
        if clothes_dict.get(kind):
            clothes_dict[kind]+=1
        else:
            clothes_dict[kind]=1
    
    for k,v in clothes_dict.items():
        answer*=(v+1)
    answer-=1
    return answer