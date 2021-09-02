import re
from itertools import permutations
def solution(expression):
    answer = 0
    expression=re.split("([+*-])",expression)
    print(expression)
    sign=["+","-","*"]
    sign_cases=list(permutations(sign,3))
    print(sign_cases) 
    result=[]
    for case in sign_cases:
        exp=expression[:]
        for op in case:
            while op in exp:
                idx=exp.index(op)
                val=str(eval(exp[idx-1]+op+exp[idx+1]))
                del exp[idx:idx+2]
                exp[idx-1]=val

            print(exp)
        result.append(abs(int(exp[0])))
    answer=max(result)            
    # case + 로시작 c1(+ - *) c2(+ * -)
    # case - 로시작 c3(- + *) c4(- * +)
    # case * 로 시작c5(* + -) c6(* - +)
   
    return answer

print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))