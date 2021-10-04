
def exec(arr,idx,c,stack):
    cur_idx=idx
    if c[0]=="D":
        c=c.split()
        val=int(c[1])
        cur_idx+=val
    elif c[0]=="U":
        c=c.split()
        val=int(c[1])
        cur_idx-=val
    elif c[0]=="C":
        stack.append((cur_idx,arr[cur_idx]))
        if cur_idx==len(arr)-1:
            del arr[cur_idx]
            cur_idx-=1
        else:
            del arr[cur_idx]
        
    elif c[0]=="Z":
        idx,val=stack.pop()
        arr.insert(idx,val)
        if idx<=cur_idx:
            cur_idx+=1
    return cur_idx



def solution(n, k, cmd):
    answer = ''
    # step 1
    arr=[i for i in range(n)]
    cur_loc=k
    stack=[]
    for c in cmd:
        cur_loc=exec(arr,cur_loc,c,stack)
        print(cur_loc)
        print(arr)
        print(stack)
    stack_num=[]
    while stack:
        idx,val=stack.pop()
        stack_num.append(val)
    
    for i in range(n):
        if i in stack_num:
            answer+="X"
            continue
        answer+="O"
    

    return answer


# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# n	k	cmd	result
# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	"OOOOXOOO"
# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	"OOXOXOOO"ß