# 상태 유저아이디 닉네임
# 닉네임 변경은 Enter Change에서 가능 (아이디가 다를 때에 같은 닉네임 있을 수 있다)
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# 정답 : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# 접근 방법 : id에 따른 최종 닉네임을 저장하기 위해 dict (id:닉네임)이용하고, (상태,id)를 순서대로 리스트에 저장해놓은 후
# 상태에 따른 문구, Enter일 경우 님이 들어왔습니다. Leave일 경우 님이 나갔습니다. Change일 경우 뛰어 넘기(닉네임 바꿔줄 때만 사용)
def solution(record):
    answer = []
    state_dict={"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    #id:닉네임 저장
    id_nick_dict={}
    log_arr=[]
    for infos in record:
        info=infos.split()
        state=info[0]
        userid=info[1]
        # leave일 경우에는 닉네임 설정이 안되기 때문에 닉네임 설정가능한 경우에만 닉네임을 바꿔준다
        if len(info)==3:
            nick_name=info[2]
            id_nick_dict[userid]=nick_name
        # print(state,userid)
        log_arr.append((userid,state))
    for log in log_arr:
        # print(log)
        if log[1]=="Change":continue
        val=id_nick_dict[log[0]]+state_dict[log[1]]
        answer.append(val)
            
            
    return answer

print(solution(record))