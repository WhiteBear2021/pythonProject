import sys
read=sys.stdin.readline

# 수열의 갯수 N
N=int(read())

# 수열을 담은 배열
sequence_list=list(map(int,read().split()))

print(sequence_list)

d=[1]*N

for i in range(N):
    for k in range(i):
        if sequence_list[i]>sequence_list[k]: #리스트 앞을 돌면서 뒤에 숫자가 작은 
            d[i]=max(d[i],d[k]+1)
            # print(d)
            
print(max(d))