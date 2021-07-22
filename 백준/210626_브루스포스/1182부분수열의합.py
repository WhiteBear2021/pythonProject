import sys
from itertools import combinations
N,S=map(int, sys.stdin.readline().split())
arr=list(map(int, input().split()))
cnt=0
for i in range(1,N+1):
    new_h_arr=list(combinations(arr,i))
   
    for val in new_h_arr:
        sum=0
        for v in val:
            sum+=v
        if sum==S:cnt+=1 
    
print(cnt)