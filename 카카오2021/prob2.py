import re
from math import sqrt
def convert(n,k):
    a = '' # 바뀐 진법
    while n > 0:
        n, mod = divmod(n, k)
        a +=str(mod)
    return a[::-1]

def solution(n, k):

    a=convert(n,k)
    a=re.sub("([0])"," ",a)
    print(a)
    print(a.split())
    a=[int(v) for v in a.split()]
    print(a)
    prime = []
    for i in a:
        if i==1:continue
        flag = True
        for j in range(2, round(sqrt(i)+1)):
            if i%j == 0: 
                flag = False
                break
        if flag:
            prime.append(i)
    print(prime)
    answer = len(prime)
    return answer

# n	k	result
# 437674	3	3
# 110011	10	2
print(solution(437674,3))