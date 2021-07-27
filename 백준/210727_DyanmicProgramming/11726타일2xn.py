import sys

# 2xN 타일의 N의 값
N=int(sys.stdin.readline())
if N==1:
    print(1)
else:
    d=[0]*(N+1)
    d[1]=1
    d[2]=2

    for i in range(3,N+1):
        d[i]=(d[i-1]+d[i-2])
        
    print(d[N]%10007)