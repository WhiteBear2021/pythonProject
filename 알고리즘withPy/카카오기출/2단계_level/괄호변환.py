def parse(s):
    correct=True
    left=0
    right=0
    mystack=[]
    for i in range(len(s)):
        if s[i]=="(":
            left+=1
            mystack.append("(")
        else:
            right+=1
            if len(mystack)==0:
                correct=False
            else:
                mystack.pop()         
        if left==right:
            return i+1, correct
    return 0, False

def solution(p):
    if len(p)==0:
        return p
    
    idx,correct=parse(p)
    u=p[:idx]
    v=p[idx:]
    if correct:
        return u+solution(v)
    answer
    
    answer = ''
    return answer

p="()))((()"
print(solution(p))