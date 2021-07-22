n=int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
# num_set=set([])
num=0
for i in range(n):
    for j in range(n):
        if i==j:continue
        arr.append(sum(arr[:(j+1)])+arr[j])
    # print(arr)
num_set=set(arr)
print(num_set)    
# print(arr)
