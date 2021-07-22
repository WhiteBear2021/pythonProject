from itertools import combinations

n=int(input())
arr = list(map(int, input().split()))
# print(arr)
num_arr=[]
num=0
for j in range(n):
    for i in list(combinations(arr, j+1)):
        if sum(i) not in num_arr:
            num_arr.append(sum(i))
num_arr.sort()
print(num_arr)
com_num=1
for i in num_arr:
    if i==com_num:
        com_num+=1
    else:
        print(com_num)
        break
else:
    print(com_num)

# print(num_arr)
# max_num=arr[n-1]
# # print(max_num)
# for k in range(len(num_arr)):
#     if k==len(num_arr)-1:
#         print(num_arr[k]-num_arr[k+1])
#         max_num=num_arr[k]+1
#         # print(max_num)
#         break
#     if num_arr[k]-num_arr[k+1]<-1:
#         # print(num_arr[k]-num_arr[k+1])
#         max_num=num_arr[k]+1
#         # print(max_num)
#         break
# else:
#     max_num+=1
#     # print(max_num)
# print(max_num)