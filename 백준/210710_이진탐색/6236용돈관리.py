import sys

# N일, M번 출금
# 7 5
N,M=map(int,sys.stdin.readline().split())

# N일동안 하루동안 사용할 금액
# 100 400 300 100 500 101 401
money_list=[int(sys.stdin.readline().strip()) for _ in range(N)]
max_money,min_money=sum(money_list),max(money_list)

while min_money<=max_money:
    mid_money=(max_money+min_money)//2
    # M값이랑 비교할 count
    count=0
    # 출금할 금액 변수 설정 
    withdrawal_money=0
    # 금액 리스트 돌면서 출금할 금액(withdrawal_money)이 금액(money)보다 적게 남을 때 withdrawal_money=mid_money로 출금하고, count 1증가 
    for money in money_list:
        if withdrawal_money<money:
            withdrawal_money=mid_money
            count+=1
        withdrawal_money-=money
    # count가 M보다 작거나 같을 경우 출금을 적게해도 될 정도로 큰 금액이라 생각하여
    # mid_money값을 작게 해주기위해 max_money값을 mid_money-1로 
    # count가 M보다 큰 경우는 출금할 금액이 낮아서 주어진 횟수보다 많이 출금해야한다 생각하여 
    # mid_money값을 크게 해주기위해 min_money값을 mid_money+1로 해주었다.
    if count<=M:
        max_money=mid_money-1
    else:
        min_money=mid_money+1
    
    # 조건문 탈출하였을 때 최소일때 값이 필요
    # min_money값을 출력
print(min_money)