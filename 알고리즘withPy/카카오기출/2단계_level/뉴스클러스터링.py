def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    str1_=[]
    str2_=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_.append(str2[i]+str2[i+1])
    
    a1 = str1_.copy(); a2 = str1_.copy()
    for i in str2_:
        a2.append(i) if i not in a1 else a1.remove(i)
    print(a2)
    common = []

    for i in str2_:
        if i in str1_: str1_.remove(i); common.append(i)
    print(common)
    
    if len(a2)==0:
        answer=65536
    else:
        answer=int(len(common)/len(a2)*65536)
    return answer

print(solution("FRANCE+","french"))