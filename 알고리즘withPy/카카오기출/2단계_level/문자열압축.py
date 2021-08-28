import re
def solution(s):
    # 처음 문자열 길이 n
    n=len(s)
    # 초기값을 n으로 설정(1로 잘랐을 경우)
    answer = n
    # 자를 문자열 길이 정하기 n의 약수여야하니까 n%i==0인경우만 길이로 설정
    for i in range(1,(n+1)//2+1):
            length=i
            # 문자를 길이 만큼 자른 list
            str_list=[s[j:j+length] for j in range(0, len(s), length)]
            print(length,"개로 쪼갰을 때:",str_list)
            cnt=1
            result=""
            for j in range(1,len(str_list)):
                if str_list[j-1]==str_list[j]:
                    cnt+=1
                else:
                    if cnt==1:
                        result+=str_list[j-1]
                    else:
                        result+=str(cnt)+str_list[j-1]
                    cnt=1
            if cnt==1:
                result+=str_list[len(str_list)-1]
            else:
                result+=str(cnt)+str_list[len(str_list)-1]
            print(len(result))
            if len(result)<answer:
                answer=len(result)
            print(result)
    return answer

# print(solution("aabbaccc"))
# print(solution("abcabcabcabcdededededede"))
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))