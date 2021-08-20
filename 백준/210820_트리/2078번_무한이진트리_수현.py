import sys
input=sys.stdin.readline

# L,R 좌표
a,b=map(int,input().split())
L,R=0,0
while a!=1 or b!=1:
    if a<b:
        b-=a
        R+=1
    else:
        a-=b
        L+=1
print(L,R)
