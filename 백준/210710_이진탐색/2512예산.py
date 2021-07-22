import sys
# 나무갯수 N개, 필요한 나무 길이 M
N= int(sys.stdin.readline())
list_N = sorted(map(int, sys.stdin.readline().split()))
M= int(sys.stdin.readline())

h_val,l_val=list_N[-1],1
    # print(h_val,l_val,N,M)
while l_val <= h_val:
    mid = (l_val+h_val)//2
    total=0
    for i in list_N:
        if i>mid:
            total+=mid
        else:
            total+=i
    if total> M:
        h_val = mid-1
    else :
        l_val = mid+1

print(h_val)
