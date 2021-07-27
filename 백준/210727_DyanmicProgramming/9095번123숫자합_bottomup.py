import sys
# test case 갯수 T
# bottomup
sys.setrecursionlimit(10**6)
T=int(sys.stdin.readline())

num_arr=[int(sys.stdin.readline()) for _ in range(T)]
d=[0]*12
d[1]=1
d[2]=2
d[3]=4

for i in range(4,12):
    d[i]=d[i-1]+d[i-2]+d[i-3]

for num in num_arr:
    print(d[num])