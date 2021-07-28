import sys
read=sys.stdin.readline


# 카드의 갯수 N
N=int(read())
# 카드 가격 pi (p1은 카드 한개묶음 가격 p2는 카드 두개 묵음 가격)
p=[0]+list(map(int,read().rstrip().split()))

# print(p)
d=[0]*(N+1)

for n in range(N+1):
    for i in range(n+1):
        d[n]=max(d[n],d[n-i]+p[i])
        # print(d)
        
print(d[N])