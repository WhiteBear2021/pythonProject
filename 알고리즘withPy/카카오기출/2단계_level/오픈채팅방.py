# 제한사항
# record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
# 다음은 record에 담긴 문자열에 대한 설명이다.
# 모든 유저는 [유저 아이디]로 구분한다.
# [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
# [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
# [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
# 첫 단어는 Enter, Leave, Change 중 하나이다.
# 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
# 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
# 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

	
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
# 결과 값 : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    state_dic={"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    # id:닉네임
    info_dic=dict()
    # 출력 상태 및 정보 저장할 리스트
    state_list=[]
    for r in record:
        print(r)
        info=r.split()
        state=info[0]
        id=info[1]
        if len(info)==3:
            nick=info[2]
            info_dic[id]=nick
        state_list.append((id,state))
    for s in state_list:
        if s[1]=="Change":continue
        word=info_dic[s[0]]+state_dic[s[1]]
        answer.append(word)
    print(answer)
    print(info_dic)
        
    return answer

solution(record)