import re
def sum(s):
    # 1. + 부호 앞 뒤에 숫자가 있을 때 +를 감싸는 괄호 만들기
    # 2. + 부호 앞에 )가 있을 경우 그 앞에 있는 (까지 포함시키는 괄호만들기
    # 3. + 부호 뒤에 (가 있을 경우 그 뒤에 있는 )까지 포함시키는 괄호 만들기
    return re.sub(r"([0-9]+\+[0-9]+|[(].+[)]\+[0-9]+|[0-9]+\+[(].+[)])","(\g<1>)",s)
def sub(s):
    # 1. - 부호 앞 뒤에 숫자가 있을 때 +를 감싸는 괄호 만들기
    # 2. - 부호 앞에 )가 있을 경우 그 앞에 있는 (까지 포함시키는 괄호만들기
    # 3. - 부호 뒤에 (가 있을 경우 그 뒤에 있는 )까지 포함시키는 괄호 만들기
    return re.sub(r"([0-9]+\-[0-9]+|[(].+[)]\-[0-9]+|[0-9]+\-[(].+[)])","(\g<1>)",s)
def mul(s):
    # 1. * 부호 앞 뒤에 숫자가 있을 때 +를 감싸는 괄호 만들기
    # 2. * 부호 앞에 )가 있을 경우 그 앞에 있는 (까지 포함시키는 괄호만들기
    # 3. * 부호 뒤에 (가 있을 경우 그 뒤에 있는 )까지 포함시키는 괄호 만들기
    return re.sub(r"([0-9]+\*[0-9]+|[(].+[)]\*[0-9]+|[0-9]+\*[(].+[)])","(\g<1>)",s)

def solution(expression):
    answer = 0
    # case + 로시작 c1(+ - *) c2(+ * -)
    c1=mul(sub(sum(expression)))
    c2=sub(mul(sum(expression)))

    # case - 로시작 c3(- + *) c4(- * +)
    c3=mul(sum(sub(expression)))
    c4=sum(mul(sub(expression)))
    # case * 로 시작 c5(* + -) c6(* - +)
    c5=sub(sum(mul(expression)))
    c6=sum(sub(mul(expression)))
    print(c1,c2,c3,c4,c5,c6)
    c1=abs(eval(c1))
    c2=abs(eval(c2))
    c3=abs(eval(c3))
    c4=abs(eval(c4))
    c5=abs(eval(c5))
    c6=abs(eval(c6))
    print(c1,c2,c3,c4,c5,c6)
    answer=max(c1,c2,c3,c4,c5,c6)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))