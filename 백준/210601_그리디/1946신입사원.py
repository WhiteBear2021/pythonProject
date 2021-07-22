import sys

result_arr=[]
test_num=int(sys.stdin.readline())
for i in range(test_num):
    result=0
    ppl_num=int(input())
    nums_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(ppl_num)]
    nums_arr.sort(key=lambda x:-(x[0]+x[1]))
    # print(nums_arr)
    com_rank=min(nums_arr[0])
    result=0
    for i in range(1,len(nums_arr)):
        if com_rank>=nums_arr[i][0] and com_rank>=nums_arr[i][1]:
            # print(nums_arr[i][0],nums_arr[i][1])
            result+=1
    result_arr.append(result)
    
for r in result_arr:
    print(r)
        
    


# n=int(input())
# nums_arr = [list(map(int, input().split())) for _ in range(n)]
# nums_arr.sort(key=lambda x:-(x[0]+x[1]))
# print(nums_arr)
# com1=nums_arr[0][0]
# com2=nums_arr[0][1]
# result=0
# for i in range(1,len(nums_arr)):
#     if com1>nums_arr[i][0] and com2>nums_arr[i][1]:
#         print(nums_arr[i][0],nums_arr[i][1])
#         result+=1
# print(result)