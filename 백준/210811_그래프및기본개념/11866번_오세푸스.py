import sys
input=sys.stdin.readline

N,M=map(int,input().split())

num_list=[i+1 for i in range(N)]
# print(num_list)

# 3이동 체크
check_cnt=0

# 답 담을 list 
result_list=[]

while True:
    if len(result_list)==N:
        break
    for i in range(N):
        if num_list[i]!=0:
            check_cnt+=1
            if check_cnt==M:
                result_list.append(num_list[i])
                num_list[i]=0
                check_cnt=0

print("<",end="")
for j in range(N):
    if j==N-1:
        print(f"{result_list[j]}>")
        break
    print(result_list[j],end=", ")