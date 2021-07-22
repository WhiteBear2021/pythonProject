import sys
from itertools import permutations

N=int(sys.stdin.readline())
num_arr=list(map(int, input().split()))
mark_num_arr=list(map(int, input().split()))
m_arr=["+","-","*","/"]
mark_arr=[]
for i in range(len(mark_num_arr)):
    for j in range(mark_num_arr[i]):
        mark_arr.append(m_arr[i])
        
# print(num_arr)
# print(mark_arr)
# print(mark_arr)
new_arr=list(permutations(mark_arr,N-1))
# print(new_arr)
sum_arr=[]
min_val=1000
max_val=0
for com in new_arr:
    # print(com)
    for _ in range(N):
        if _==0:
            sum=num_arr[_]
        elif _==N-1:break
        
        if com[_]=="+":
            sum=int(sum+num_arr[_+1])
        elif com[_]=="-":
            sum=int(sum-num_arr[_+1])
        elif com[_]=="*":
            sum=int(sum*num_arr[_+1])
        else:
            sum=int(sum/num_arr[_+1])
    if sum>max_val:
        sum=max_val
    if sum<min_val:
        sum=min_val
            
print(max_val)
print(min_val)
# print(sum_arr)
# sum_arr.sort()
# print(sum_arr[0])
# print(sum_arr[-1])
# print(max(sum_arr))
# print(min(sum_arr))