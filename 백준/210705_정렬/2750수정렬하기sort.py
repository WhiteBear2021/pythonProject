import sys

N=int(sys.stdin.readline())
num_arr=[]
for i in range(N):
    num_arr.append(int(sys.stdin.readline()))
    
num_arr.sort()
for num in num_arr:
    print(num)