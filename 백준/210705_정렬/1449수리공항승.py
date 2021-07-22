# N은 테이프 갯수 M은 테이프 길이
N,M=map(int, input().split())

leak_loc_arr=list(map(int, input().split()))
leak_loc_arr.sort()
# print(leak_loc_arr)

tape_loc=0
tape_cnt=0
for _ in range(len(leak_loc_arr)):
    if _==0:
        tape_loc=leak_loc_arr[_]+M
        tape_cnt=1
        continue
        
    if leak_loc_arr[_]<tape_loc:
        continue
    else:
        tape_loc=leak_loc_arr[_]+M
        tape_cnt+=1
print(tape_cnt)
    



