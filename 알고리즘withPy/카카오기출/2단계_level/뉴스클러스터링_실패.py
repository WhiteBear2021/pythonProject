def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    # 한 리스트에 몇개씩 담을지 결정
    n = 2
    str1 = [str1[i * n:(i + 1) * n] for i in range((len(str1) + n - 1) // n )] 
    str2 = [str2[i * n:(i + 1) * n] for i in range((len(str2) + n - 1) // n )] 
    print(str1)
    print(str2)
    str1=[str1[i] for i in range(len(str1)) if str1[i].isalpha() and len(str1[i])==2]
    str2=[str2[i] for i in range(len(str2)) if str2[i].isalpha() and len(str2[i])==2]
    print(str1)
    l1=len(str1)
    l2=len(str2)
    
    a1 = str1.copy(); a2 = str1.copy()
    for i in str2:
        a2.append(i) if i not in a1 else a1.remove(i)
    print(a2)
    common = []

    for i in str2:
        if i in str1: str1.remove(i); common.append(i)
    print(common)
    
    answer=int(len(common)/len(a2)*65536)
    return answer

print(solution("FRANCE+","french"))