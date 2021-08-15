# 3번문제

import re
def solution(amountText):
    answer = False
    p1 = re.compile('[a-z]+')
    p2 = re.compile('^[1-9]/d')
        m = p1.match(amountText)
        if m:
            print('Match found: ', m.group())
        else:
            print('No match')

    return answer
