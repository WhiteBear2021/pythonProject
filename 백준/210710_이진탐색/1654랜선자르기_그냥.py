import sys
from typing import AnyStr
# 내가 가진 랜선 갯수 N, 같은 길이로 만들어야하는 랜선 갯수 K
N, K = map(int, sys.stdin.readline().split())
n=K//N
# 내가 가진 랜선의 길이 리스트로
list_N=list(int(sys.stdin.readline()) for _ in range(N))

# print(list_N)
high_val,low_val=sum(list_N)//N,1
print(high_val,low_val)
# print(val)
while low_val<=high_val:
    chk_val=(high_val+low_val)//2
    cnt_val=sum([x//chk_val for x in list_N])
    if cnt_val<N:
        high_val=chk_val-1
    elif cnt_val>=N:
        low_val=chk_val+1
        ans=chk_val
        
print(ans)
