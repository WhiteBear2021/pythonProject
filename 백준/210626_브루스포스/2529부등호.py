import sys
num=int(sys.stdin.readline())
mark_arr=sys.stdin.readline().split()
arr1=[0,1,2,3,4,5,6,7,8,9]
arr2=[9,8,7,6,5,4,3,2,1,0]
min_arr=arr1[0:num+1]
max_arr=arr2[0:num+1]
# 최소 구하기
min_idx=0
min_ans=[]
count=0
for i in range(len(mark_arr)):
    if mark_arr[i]=="<":        
        if count!=0:
            for _ in range(min_idx+count,min_idx-1,-1):
                min_ans.append(min_arr[_])
            min_idx=min_idx+count+1
        else:
            min_ans.append(min_arr[min_idx])
            min_idx+=1        
        count=0
    else:
        count+=1
if count!=0:
    for _ in range(min_idx+count,min_idx-1,-1):
            min_ans.append(min_arr[_])
            min_idx=min_idx+count+1
else:
    min_ans.append(min_arr[min_idx])        

    
# 최대 구하기
max_idx=0
max_ans=[]
count=0
for i in range(len(mark_arr)):
    if mark_arr[i]==">":        
        if count!=0:
            for _ in range(max_idx+count,max_idx-1,-1):
                max_ans.append(max_arr[_])
            max_idx=max_idx+count+1
        else:
            max_ans.append(max_arr[max_idx])
            max_idx+=1        
        count=0
    else:
        count+=1
if count!=0:
    for _ in range(max_idx+count,max_idx-1,-1):
            max_ans.append(max_arr[_])
            max_idx=max_idx+count+1
else:
    max_ans.append(max_arr[max_idx])       
    
for max in max_ans:
    print(max,end="")
print()
for min in min_ans:
    print(min,end="")

