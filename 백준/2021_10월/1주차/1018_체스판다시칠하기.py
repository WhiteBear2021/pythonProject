# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
def compare_arrs_color(pivot_arr,array):
    count=0
    for i in range(len(array)):
        for ar1,ar2 in zip(pivot_arr[i], array[i]):
            if ar1!=ar2:
                count+=1
    return min(count,64-count)
        

def count_change_color(array):
    pivot_arr_Black=[[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]
    pivot_arr_White=[[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]
    result1=compare_arrs_color(pivot_arr_Black,array)
    result2=compare_arrs_color(pivot_arr_White,array)
    return min(result1,result2)

N,M=map(int,input().split())
arr=[]
for _ in range(N):
    val=input()
    val=val.replace("W","0").replace("B","1")
    arr.append(list(map(int,val)))
    
# print(arr)
answer=64

for i in range(len(arr)-7):
    for j in range(len(arr[i])-7):
        result=count_change_color(arr[i:i+8][j:j+8])
        if result<answer:
            answer=result

print(answer)

# 9 10
# BBBBBBBBBB
# BWWBWBWBWB
# BWBWBWBWBW
# BWWBWBWBWB
# BWBWBBBWBW
# BWWBWBWBWB
# BWBWBWBWBW
# BWWBWBWBWB
# BWBWBWBWBW