# True False 소대문자 확인
# for 값을 먼저 넣고 for문을 돌려야함.(이렇게하면 효율성 아웃)
def solution(phone_book):
    answer = True
    # phone_dict={}
    length=len(phone_book)
    # for i in range(length):
    #     phone_dict[i]=phone_book[i]
    # print(phone_dict)
    for phone in phone_book:
        for i in range(length):
            if phone.startswith(phone_book[i]):
                return False
    
    return answer
a=["119", "97674223", "1195524421"]
# 결과 false
print(solution(a))