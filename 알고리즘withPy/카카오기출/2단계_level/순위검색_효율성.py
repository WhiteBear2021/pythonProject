def solution(info, query):
    answer = []
    for q in query:
        qu=q.replace("and","").split()
        ppl_cnt=0
        for i in info:
            data=i.split()
            if (data[0]==qu[0] or qu[0]=="-") and (data[1]==qu[1] or qu[1]=="-") and (data[2]==qu[2] or qu[2]=="-") and(data[3]==qu[3] or qu[3]=="-") and(qu[4]=="-" or int(qu[4])<=int(data[4])):
                ppl_cnt+=1
        answer.append(ppl_cnt)
    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))
