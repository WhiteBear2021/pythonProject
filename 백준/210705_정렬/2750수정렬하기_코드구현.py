import sys

N=int(sys.stdin.readline())
num_arr=[]
for i in range(N):
    num_arr.append(int(sys.stdin.readline()))
    
for idx in range(len(num_arr)-1):
    for c_idx in range(idx+1,len(num_arr)):
        if num_arr[idx]>num_arr[c_idx]:
            print(num_arr[idx],num_arr[c_idx])
            num_arr[idx],num_arr[c_idx]=num_arr[c_idx],num_arr[idx]
            
for num in num_arr:
    print(num)