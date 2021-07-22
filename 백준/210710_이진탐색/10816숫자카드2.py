# https://chancoding.tistory.com/45
import sys
# 주어진 숫자카드 갯수
N = int(sys.stdin.readline())
# 주어진 숫자카드 리스트
list_N = sorted(map(int, sys.stdin.readline().split()))
# 확인할 숫자카드 갯수
M = int(sys.stdin.readline())
# 확인할 숫자카드 리스트
list_M = list(map(int, sys.stdin.readline().split()))
# print(list_N)
# -10 -10 2 3 3 6 7 10 10 10

# 이진 탐색 함수
def is_existing_target_num(target_num,array):
    # print(target_num)
    # print(array)
    cur_min_idx=0
    cur_max_idx=len(array)-1
    cnt=0
    while cur_min_idx<=cur_max_idx:
        cur_guess_idx=(cur_min_idx+cur_max_idx)//2
        if target_num==array[cur_guess_idx]:
            return array[0:len(array)].count(target_num)
            # chk_guess_idx1=cur_guess_idx
            # chk_guess_idx2=cur_guess_idx
            # # guess_idx 작게해보기
            # while 0<chk_guess_idx1<N:
            #     if target_num==array[chk_guess_idx1-1]:
            #         cnt+=1
            #         chk_guess_idx1-=1
            #     else:
            #         break
            # # guess_idx 크게해보기
            # while 0<=chk_guess_idx2<N-1:
            #     if target_num==array[chk_guess_idx2+1]:
            #         cnt+=1
            #         chk_guess_idx2+=1
            #     else:
            #         break
            # break
        elif array[cur_guess_idx]<target_num:
                cur_min_idx=cur_guess_idx+1
        else:
            cur_max_idx=cur_guess_idx-1
    # print(f"cnt값 {cnt}")
    return cnt

for chk_num in list_M:
    # print(chk_num,list_N)
    print(is_existing_target_num(chk_num,list_N),end=" ")
