import sys
# 숫자 갯수 N
N=int(sys.stdin.readline())

num_arr=list(map(int,sys.stdin.readline().split()))
num_arr.sort()
# print(num_arr)

result=0
for i in range(N):
    if result+1>=num_arr[i]:
        result+=num_arr[i]
    else:
        break

print(result+1)

result=0
for i in range(N):
    if result+1>=num_arr[i]:
        print(result+1,num_arr[i])
        result=sum(num_arr[:i+1])
        print(result)
    else:
        break
    print()
print(result+1)