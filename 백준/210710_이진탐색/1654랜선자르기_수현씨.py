import sys
k, n = map(int, sys.stdin.readline().split())
lan = sorted([int(input()) for _ in range(k)])
left = 1
right = lan[-1]

while left <= right:
    total = 0
    mid = (left+right)//2
    print(mid)
    for i in lan:
        total += i//mid
    if total>= n:
        left = mid+1
    else :
        right = mid-1

print(right)