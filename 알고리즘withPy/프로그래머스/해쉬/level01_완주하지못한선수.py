# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

def solution(participant, completion):
    answer = ''
    race_dic=dict()
    for name in participant:
        if race_dic.get(name):
            race_dic[name]+=1
        else:
            race_dic[name]=1
        # print(race_dic)
            
    for name in completion:
        race_dic[name]-=1
        # print(race_dic)   
        
    for name,num in race_dic.items():
        if num==1:
            answer=name
            break
    return answer

p=["leo", "kiki", "eden"]
c=	["eden", "kiki"]
print(solution(p,c))
# 정답 : leo