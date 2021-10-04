def chg_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n, t, m, p):
        answer = ''
        order=0
    
        for num in range(16):
            s=str(chg_n(num,n))
            print(s)
            for i in s:
                order+=1
                if order%m==p:
                    answer+=i
                    if len(answer)==t:
                        return answer
        return answer
    
print(solution(16,16,2,2))
# "13579BDF01234567"