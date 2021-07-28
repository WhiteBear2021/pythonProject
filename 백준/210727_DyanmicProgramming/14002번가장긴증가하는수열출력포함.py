import sys
read=sys.stdin.readline

N=int(read())

sequence_list=list(map(int,read().split()))

print(sequence_list)

d=[1]*N

for i in range(N):
    for k in range(i):
        if sequence_list[i]>sequence_list[k]:
            d[i]=max(d[i],d[k]+1)
            print(d)
            
print(max(d))