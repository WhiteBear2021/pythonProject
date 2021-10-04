def solution(info, query):
    answer = []
    for q in query:
        q1,q2,q3,g=q.split("and")
        q4,q5=g.split()
        q1=q1.strip()
        q2=q2.strip()
        q3=q3.strip()
        ppl_cnt=0
        for i in info:
            chk_cnt=0
            lan,area,career,food,grade=i.split()
            if q1=="-" or q1==lan:
                chk_cnt+=1
                # print(q1,lan)
            if q2=="-" or q2==area:
                chk_cnt+=1
                # print(q2,area)
            if q3=="-" or q3==career:
                chk_cnt+=1
                # print(q3,career)
            if q4=="-" or q4==food:
                chk_cnt+=1
                # print(q4,food)
            if q5=="-" or int(q5)<=int(grade):
                chk_cnt+=1
                # print(q5,grade)
            # print(chk_cnt)
            if chk_cnt==5:
                ppl_cnt+=1
        answer.append(ppl_cnt)
    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))
