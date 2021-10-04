# 5457
# 3
# 6 7 8

num=input()
bnum=int(input())
broken_nums=map(int,input().split())
answer=0
if num=="100":
    print(answer)
else:
    for n in num:
        if n in broken_nums:
            