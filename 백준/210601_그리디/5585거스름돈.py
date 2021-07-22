pay_price=int(input())
remain_price=1000-pay_price
remain=[ 500, 100, 50, 10, 5, 1 ]
cnt=0
for r in remain:
    a,remain_price=divmod(remain_price,r)
    cnt+=a
    if remain_price==0:break
print(cnt)
