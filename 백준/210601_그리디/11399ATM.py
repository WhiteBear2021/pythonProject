n=int(input())

arr = list(map(int, input().split()))
def plus(idx,array):
    result=0
    for i in range(idx+1):
        result+=array[i]
    return result


# print(arr)
arr.sort()
sum=0
for i in range(len(arr)):
    sum+=plus(i,arr)
print(sum)

