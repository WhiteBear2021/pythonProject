n=int(input())
# nums_arr=[input().split() for _ in range(n)]
# nums_arr=[list(map(int, input())) for _ in range(n)]
nums_arr = [list(map(int, input().split())) for _ in range(n)]
nums_arr.sort()
print(nums_arr)

# for i in range(len(nums_arr)):
#     print(nums_arr[i][0])
#     print(nums_arr[i][1])



max_length=0
for i in range(len(nums_arr)):
    compare_arr=[]
    compare_arr.append(nums_arr[i])
    print("첨에 추가한 배열:")
    print(compare_arr)
    start_time=nums_arr[i][0]
    end_time=nums_arr[i][1]
    for j in range(i+1,len(nums_arr)):
        print("두번째 for 문 index:"+str(j))
        print(nums_arr[j])
        if end_time<=nums_arr[j][0]:
            print("끝나는 시간:"+str(end_time))
            print("다음 시작 시간:"+str(nums_arr[j][0]))
            # 끝나는 시간이 시작시간보다 작거나 같을 때 부터 다음 시간으로 이어진다
            compare_arr.append(nums_arr[j])
        if nums_arr[j-1][0]==nums_arr[j][0]:
            nums_arr[j-1][1]>nums_arr[j][1]
            compare_arr[j-1]=nums_arr[j]
            print("for 문 안에")
            print(nums_arr[j])
            # 이전 회의 시작 시간이랑 같을 때, 끝나는 시간이 더 일찍 끝날때 교체
        end_time=compare_arr[j][1]
if max_length<len(compare_arr):
    max_length=len(compare_arr)
    print("최대 길이:"+max_length)
