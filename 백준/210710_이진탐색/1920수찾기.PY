import sys
def is_existing_target_num(target,array):
    cur_min_idx=0
    cur_max_idx=len(array)-1

    while cur_min_idx<=cur_max_idx:
        cur_guess=(cur_min_idx+cur_max_idx)//2
        if array[cur_guess]==target:
            return 1
        elif array[cur_guess]<target:
            cur_min_idx=cur_guess+1
        else:
            cur_max_idx=cur_guess-1
    return 0


# A집합 숫자 갯수
N=int(sys.stdin.readline())

num_arr=list(map(int, sys.stdin.readline().split()))
num_arr.sort()
# 찾을 숫자 갯수
M=int(sys.stdin.readline())
find_num_arr=list(map(int, sys.stdin.readline().split()))

# print(num_arr)
# print(find_num_arr)

for finding_num in find_num_arr:
    print(is_existing_target_num(finding_num,num_arr))
