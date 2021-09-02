def solution(priorities, location):
    answer = 0
    docu_list=[]
    for i in range(len(priorities)):
        docu_list.append((priorities[i],i))
    order=sorted(priorities,reverse=True)
    for ord in order:
        for docu in docu_list:
            p,i=docu_list.pop(0)
            print(p,i,ord,location)
            print(docu_list)
            if p==ord:
                answer+=1
                if i==location:
                    return answer
                else:break
            else:
                docu_list.append((p,i))
                
    return answer

# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
print(solution([2, 1, 3, 2],2))