# 4
# 1 2 3 4

# 5
# 5 4 3 2 1
from itertools import permutations

# 숫자갯수 N
N=int(input())

nums=list(map(int,input().split()))
nums_copy=nums[::]
nums_copy.sort()
nums_permutations=list(permutations(nums_copy,N))
if list(nums_permutations[-1])==nums:
    print(-1)
else:
    for i in range(len(nums_permutations)):
        print(nums,nums_permutations[i])
        if nums==list(nums_permutations[i]):
            for num in nums_permutations[i+1]:
                print(num,end=" ")
            break