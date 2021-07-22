import sys
N,score,length=map(int, sys.stdin.readline().split())
# print(N,score,length)
if N==0:
    rank=1
else:
    score_arr=list(map(int, sys.stdin.readline().split()))
    # print(score_arr)
    idx_arr=[]
    for i in range(len(score_arr)):
        if score_arr[i]==score:
            idx_arr.append(i+1)
    # 제일 먼저 들어간 순위 m, 제일 마지막 들어간 순위 M
    m=idx_arr[0]
    M=idx_arr[-1]
    print(idx_arr)
    if M<length:
        rank=m
    else:
        rank=-1

print(rank)