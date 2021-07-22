import sys
n, c = map(int, sys.stdin.readline().split())
lan = sorted([int(input()) for _ in range(n)])
left = lan[0]
right = lan[-1]-lan[0]

while left<=right:
    count = 1
    length = lan[0]
    mid = (left+right)//2
    for i in range(1,n):
        if lan[i] >= length+mid:
            length = lan[i]
            count+=1
    if count < c:
        right = mid - 1
    else:
        left = mid + 1

print(right)