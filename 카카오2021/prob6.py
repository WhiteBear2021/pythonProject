def solution(board, skills):
    answer = 0
    col_len=len(board[0])
    idx_dict={}
    for skill in skills:
        type,r1,c1,r2,c2,degree=skill
        start=r1*col_len+c1
        end=r2*col_len+c2
        print(skill)
        print(start,end)
        if type==1:
            for i in range(start,end+1):
                if c1<=(i%col_len)<=c2:
                    if idx_dict.get(i):
                        idx_dict[i]=idx_dict[i]-degree
                    else:
                        idx_dict[i]=-degree
        elif type==2:
            for i in range(start,end+1):
                if c1<=(i%col_len)<=c2:
                    if idx_dict.get(i):
                        idx_dict[i]=idx_dict[i]+degree
                    else:
                        idx_dict[i]=degree
        print(idx_dict)
    print(idx_dict)
    for k,v in idx_dict.items():
        i,j=divmod(k,col_len)
        board[i][j]+=v
    print(board)
    # for b in board:
    #     for v in b:
    #         if v>0:
    #             answer+=1
    list_=sum(board,[])
    # answer=len([i for i in list_ if i>0])
    answer = len(list(filter(lambda x: x > 0, list_)))
    return answer

# board	skill	result
# [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	10
# [[1,2,3],[4,5,6],[7,8,9]]	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	6
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))