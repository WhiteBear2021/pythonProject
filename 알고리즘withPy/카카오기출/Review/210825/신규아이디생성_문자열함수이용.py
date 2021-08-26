# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    answer = ''
    # 1. 소문자 처리 lower
    new_id=new_id.lower()
    
    # 2. 알파벳과 숫자, - _ . 를 제외하고 제거 isalnum() 숫자 알파벳인지 찾는 함수, isalpha() 알파벳인지, isdigit() 숫자인지
    for s in new_id:
        if s.isalnum() or s in ["-","_","."]:
            answer+=s
    print(new_id)
    print(answer)
    # 3. .이 두번이상이라면 .하나로 바꿔주기 replace(찾을형식의문자,최종변경될문자형태)
    while ".." in answer:
        answer=answer.replace("..",".")
    print(answer)
    # 4. .이 처음이나 끝에 위치하면 제거
    if answer.startswith("."):
        answer=answer[1:]
    if answer.endswith("."):
        answer=answer[:-1]
    # 5. 빈 문자열이면 a 추가
    if len(answer)==0:
        answer="aaa"
    # 6. 16자이상이면 15자리까지, 15자리가 .이라면 .을 제거
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]==".":
            answer=answer[:14]
    # 7. 2글자 이하라면 3글자 될때까지 마지막 글자 추가 시켜준다
    if len(answer)<=2:
        answer=answer+answer[-1]*(3-len(answer))
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))