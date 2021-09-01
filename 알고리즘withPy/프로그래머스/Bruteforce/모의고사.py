def solution(answers):
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    g_1=0
    g_2=0
    g_3=0
    grade_info={1:0,2:0,3:0}
    # print(grade_info)
    for i in range(len(answers)):
        a=answers[i]
        na1=i%len(a1)        
        na2=i%len(a2)        
        na3=i%len(a3)
        if a==a1[na1]:
            grade_info[1]+=1
        if a==a2[na2]:
            grade_info[2]+=1
        if a==a3[na3]:
            grade_info[3]+=1
    grade=sorted(grade_info.items(), key = lambda item: item[1], reverse=True)
    # print(grade)
    val=grade[0][1]
    answer = []
    for i in grade:
        if val==i[1]:
            answer.append(i[0])
    
    return answer