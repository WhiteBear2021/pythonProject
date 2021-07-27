import sys
sys.setrecursionlimit(10**6)
# 2xN 타일의 N의 값
N=int(sys.stdin.readline())

d=[0]*(N+1)

def dp(x):
    if(x==1):return 1
    if(x==2):return 3
    if d[x]==0:
       d[x]=dp(x-1)+2*dp(x-2)
    return d[x]

print(dp(N)%10007)