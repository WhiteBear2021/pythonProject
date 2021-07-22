import sys
from itertools import combinations

N=int(sys.stdin.readline())
n=[]
for num in range(N):
    n.append(num)
m=[list(map(int, input().split())) for _ in range(N)]

comb_arr=list(combinations(n,int(N/2)))
# print(n)
# print(m)
# print(comb_arr)
result=10000
for arr in comb_arr:
    start_arr=[]
    link_arr=[]
    for idx in range(N):
        if idx in arr:
            start_arr.append(idx)
        else:
            link_arr.append(idx)
    # print(start_arr)
    # print(link_arr)
    sum_start=0
    sum_link=0
    for a in range(len(start_arr)):
        i_s=start_arr[a]
        i_l=link_arr[a]
        for b in range(len(link_arr)):
            if a==b:continue
            j_s=start_arr[b]
            j_l=link_arr[b]
            sum_start+=m[i_s][j_s]
            sum_link+=m[i_l][j_l]
    dif=abs(sum_start-sum_link)
    if dif==0:
        result=0
        break
    if dif<result:
        result=dif    
print(result)    
