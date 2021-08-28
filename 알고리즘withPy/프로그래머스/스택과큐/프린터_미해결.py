def solution(priorities, location):
    answer = 0
    queue=[]
    importance=[0]*10
    for i in range(len(importance)):
        importance[i]=priorities.count(i)
    print(importance)
    for i in range(len(priorities)):
        queue.append((priorities[i],i))
    print(queue)
    cnt=0
    for k in range(9,0,-1):
        # print(k)
        while importance[k]!=0:
            val=queue.pop(0)
            if val[0]==k:
                importance[k]-=1
                cnt+=1
                if val[1]==location:
                    return cnt
            else:
                queue.append(val)
            
    return answer
print(solution([1, 1, 9, 1, 1, 1],0))