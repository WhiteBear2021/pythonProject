# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
import re
# "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    answer = ''
    # 1. 소문자 처리 lower
    # print(new_id)
    new_id=re.sub("([A-Z])",
           lambda x:x.group(1).lower(),
           new_id)
    # print(new_id)
    # 2. 알파벳과 숫자, - _ . 를 제외하고 제거 
    new_id=re.sub("([^0-9A-Za-z-_.])","",new_id)
    # print(new_id)
    # print(answer)
    # 3. .이 두번이상이라면 .하나로 바꿔주기 replace(찾을형식의문자,최종변경될문자형태)
    new_id=re.sub("([.]{2,})",".",new_id)
    # print(new_id)
    # 4. .이 처음이나 끝에 위치하면 제거
    new_id=re.sub("((^[.]|[.]$))","",new_id)
    # print(new_id)
    # 5. 빈 문자열이면 a 추가
    if len(new_id)==0:
        new_id="aaa"
    # 6. 16자이상이면 15자리까지, 15자리가 .이라면 .을 제거
    if len(new_id)>=16:
        new_id=new_id[:15]
        new_id=re.sub("([.]$)","",new_id)
    # 7. 2글자 이하라면 3글자 될때까지 마지막 글자 추가 시켜준다
    if len(new_id)<=2:
        new_id+=new_id[-1]*(3-len(new_id))
    # print(new_id)
    answer=new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("m"))
print(solution("123_.def"))