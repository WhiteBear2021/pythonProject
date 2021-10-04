 
def next_val(array):
    n=len(array)-1
    i=n
    while i>0 and array[i-1]>=array[i]:
        i-=1
    if i<=0:
        return False
    
    j=n
    if array[i-1]>=array[j]:
        j-=1
    array[i-1],array[j]=array[j],array[i-1]
    
    k=n
    while i<k:
        array[i],array[k]=array[k],array[i]
    
    return True    
# 숫자 갯수 N
N=int(input())
# 받은 숫자 배열로 받기 arr
arr=list(map(int,input().split()))

# next_val(arr)을 통해서 True False 여부, arr는 참조변수이므로 함수에서 다음 순열 값으로 바꿔주기
if next_val(arr):
    print(' '.join(map(str,arr)))
else:
    print(-1)