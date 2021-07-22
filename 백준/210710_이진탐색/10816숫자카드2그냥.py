import sys
# 주어진 숫자카드 갯수
N = sys.stdin.readline()
# 주어진 숫자카드 리스트
list_N = list(map(int, sys.stdin.readline().split()))
# 확인할 숫자카드 갯수
M = sys.stdin.readline()
# 확인할 숫자카드 리스트
list_M = list(map(int, sys.stdin.readline().split()))
ans_arr=[]
for chk_num in list_M:
    cnt=0
    for i in range(len(list_N)):
        if chk_num==list_N[i]:
            cnt+=1
    ans_arr.append(cnt)
    
for ans in ans_arr:
    print(ans,end=" ")