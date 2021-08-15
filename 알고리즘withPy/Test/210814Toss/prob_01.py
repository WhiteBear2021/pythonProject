# 1번문제

import math

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료            
    answer = (orderAmount-serviceFee-taxFreeAmount)/11
    answer=math.ceil(answer)
    if orderAmount-serviceFee-taxFreeAmount==1:
        answer=0
    return answer