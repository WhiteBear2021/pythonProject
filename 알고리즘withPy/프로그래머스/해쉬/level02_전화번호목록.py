# True False 소대문자 확인
# for 값을 먼저 넣고 for문을 돌려야함.(이렇게하면 효율성 아웃)
def solution(phone_book):
    answer = True
    phone_num=[]
    for i in range(len(phone_book)):
        phone=phone_book[i]
        for j in range(len(phone_book)):
            if i==j:continue
            length=len(phone_book[j])
            if phone[:length]==phone_book[j]:
                answer=False
                break
    return answer