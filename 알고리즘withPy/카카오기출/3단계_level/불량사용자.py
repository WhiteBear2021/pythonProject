import re
def solution(user_id, banned_id):
    answer = 1
    banned_id=[val.replace("*",".") for val in banned_id]
    # print(banned_id)
 
    com_list=[]
    for reg in banned_id:
        p=re.compile(reg)
        cnt_list=[]
        for i in range(len(user_id)):
            m=re.search(reg,user_id[i])
            # print(id,m)
            if m==None:
                continue
            else:
                # print(m.start(),m.end(),len(id))
                if m.end()-m.start()==len(user_id[i]):
                    cnt_list.append(user_id[i])
        com_list.append(cnt_list)
    print(com_list)
    return answer


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
# user_id	banned_id	result
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3