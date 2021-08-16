import sys
input=sys.stdin.readline

# test case T
T=int(input())
for t in range(T):
    # 문서 갯수 N, 알고싶은 번호 A
    N,A=map(int,input().split())

    num_list=[[i] for i in range(N)]
    rank_list=list(map(int,input().split()))
    for j in range(N):
        num_list[j].append(rank_list[j])

    rank_list.sort(reverse=True)
    cnt=0
    # print(rank_list)
    for r in rank_list:
        while True:
            # print(num_list)
            if r==num_list[0][1]:
                print_num=num_list.pop(0)
                cnt+=1
                break
            else:
                val=num_list.pop(0)
                num_list.append(val)

        if print_num[0]==A:
            print(f"{cnt}")
            break
    