import sys
N=int(sys.stdin.readline())

neg_num_arr=[]
pos_num_arr=[]
for i in range(N):
    val=int(sys.stdin.readline()[:-1])
    if val<=0:
        neg_num_arr.append(val)
    else:
        pos_num_arr.append(val)

neg_num_arr.sort()
pos_num_arr.sort(reverse=True)   
print(neg_num_arr)
print(pos_num_arr)

sum_val=0
# 묶을 수 뒤의 index 값 : n
n=-10001
for i in range(len(neg_num_arr)):
    if i==n: continue
    if i==len(neg_num_arr)-1:
        sum_val+=neg_num_arr[i]
        break
    if neg_num_arr[i]*neg_num_arr[i+1]>=0:
        sum_val+=neg_num_arr[i]*neg_num_arr[i+1]
        n=i+1
    else:
        sum_val+=neg_num_arr[i]        
# print(sum_val)

n=10001
for i in range(len(pos_num_arr)):
    if i==n: continue
    if i==len(pos_num_arr)-1:
        sum_val+=pos_num_arr[i]
        break
    if pos_num_arr[i+1]==1:
        sum_val+=pos_num_arr[i]  
    elif pos_num_arr[i]*pos_num_arr[i+1]>0:
        sum_val+=pos_num_arr[i]*pos_num_arr[i+1]
        n=i+1
    else:
        sum_val+=pos_num_arr[i]   
print(sum_val)