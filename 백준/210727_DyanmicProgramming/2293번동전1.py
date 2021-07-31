import sys
read=sys.stdin.readline

# 동전 종류 N, 동전들로 만들어야하는 값 K
N,K=map(int,read().split())

coin_arr=[int(sys.stdin.readline()) for _ in range(N)]

d=[0]*(K+1)
d[0]=1
for c in coin_arr:
    for k in range(1,K+1):
        if k-c>=0:
            d[k]+=d[k-c]
            print(k,c,k-c)
            print(d)
            

print(d[K])