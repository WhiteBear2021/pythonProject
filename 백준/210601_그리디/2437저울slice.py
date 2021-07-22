n=int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
# num_set=set([])
sum_val=0
for i in range(-1,-len(arr)-1,-1):
    # print(sum(arr[:i]))
    if sum(arr[:i])<arr[i]:
        sum_val=sum(arr[:i])+1
    else:
        break
else:
    sum_val=sum(arr)+1
    # print()
    # print(sum_val)
print(sum_val)
    # print(i)
    # print(sum(arr[:i])-arr[i])
    # print(arr[i])
    # if sum(arr[:i])
