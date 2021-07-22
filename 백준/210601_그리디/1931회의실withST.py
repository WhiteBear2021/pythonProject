n=int(input())
# nums_arr=[input().split() for _ in range(n)]
# nums_arr=[list(map(int, input())) for _ in range(n)]
nums_arr = [list(map(int, input().split())) for _ in range(n)]
nums_arr.sort(key=lambda x:(x[1],x[0]))
# print(nums_arr)
cnt_meeting=0
start_time=0
finish_time=0
for i in range(len(nums_arr)):
    if nums_arr[i][0]>=finish_time:
        start_time=nums_arr[i][0]
        finish_time=nums_arr[i][1]
        cnt_meeting+=1
print(cnt_meeting)