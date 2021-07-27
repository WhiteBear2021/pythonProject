# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys
read=sys.stdin.readline

N=int(read())
# DP 테이블 초기화
d=[0]*(N+1)

for num in range(2,N+1):

    d[num]=d[num-1]+1
    if num%2==0:
        d[num]=min(d[num],d[num//2]+1)
    if num%3==0:
        d[num]=min(d[num],d[num//3]+1)

 
print(d[N])