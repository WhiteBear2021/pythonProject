# 3
# 3 4 5
# 2 2

# 시험장 수 n
n=int(input())

# 시험장 마다 응시인원 수
tester_list=list(map(int,input().split()))

# 총감독 감시수, 부감독 감시수
general_mgr,sub_mgr=map(int,input().split())

# print(n,tester_list,general_mgr,sub_mgr)
# 필요한 감독 수 answer
answer=0
for i in range(n):
    val=tester_list[i]
    while True:
        if val==tester_list[i]:
            val-=general_mgr
            answer+=1
        else:
            if val%sub_mgr==0:
                answer+=(val//sub_mgr)
            else:
                answer+=(val//sub_mgr)+1
            break
        if val<=0:
            break
print(answer)