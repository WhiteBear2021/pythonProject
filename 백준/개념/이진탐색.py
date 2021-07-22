finding_target_num=14
finding_number_arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# 1~16 사이의 중간값으로 시돗값 8
# 9~16 사이의 중간값으로 시돗값 12
# 13~16 사이의 중간값으로 시돗값 14 정닶

def is_existing_target_num(target,array):
    cur_min_idx=0
    cur_max_idx=len(finding_number_arr)-1

    while cur_min_idx<=cur_max_idx:
        cur_guess=(cur_min_idx+cur_max_idx)//2
        if array[cur_guess]==target:
            return 1
        elif array[cur_guess]<target:
            cur_min_idx=cur_guess+1
        else:
            cur_max_idx=cur_guess-1
    return 0


print(is_existing_target_num(finding_target_num,finding_number_arr))    