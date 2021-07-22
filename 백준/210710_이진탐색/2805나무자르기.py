import sys
# 나무갯수 N개, 필요한 나무 길이 M
N, M = map(int, sys.stdin.readline().split())

list_N = list(map(int, sys.stdin.readline().split()))
h_val,l_val=list_N[-1],1
# print(h_val,l_val)
# print(N,M,list_N[0])

while l_val <= h_val:
    mid = (l_val+h_val)//2
    # total=sum(i-mid if mid < i else 0 for i in list_N)
    for i in list_N:
        if i-mid>0:
            total += i-mid
    if total>= M:
        l_val = mid+1
    else :
        h_val = mid-1

print(h_val)