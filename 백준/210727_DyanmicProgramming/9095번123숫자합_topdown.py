import sys
# test case 갯수 T
sys.setrecursionlimit(10**6)
T=int(sys.stdin.readline())

num_arr=[int(sys.stdin.readline()) for _ in range(T)]
d=[0]*12
d[1]=1
d[2]=2
d[3]=4
def dp_topDown(x):
    if x==1:return 1
    if x==2:return 2
    if x==3:return 4
    if d[x]!=0:
        return d[x]
    
    return dp_topDown(x-1)+dp_topDown(x-2)+dp_topDown(x-3)

   
for num in num_arr:
    print(dp_topDown(num))