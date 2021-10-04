from itertools import combinations
def cal_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

# nxn 배열 n, 치킨집 갯수 m
n,m=map(int,input().split())

mylist=[list(map(int, input().split())) for _ in range(n)]

print(n,m,mylist)

house_list=[]
chicken_list=[]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        if mylist[i][j]==1:
            house_list.append([i,j])
        elif mylist[i][j]==2:
            chicken_list.append([i,j])

chicken_pick=list(combinations(chicken_list,m))
max_dist=1000
ans_arr=[0]*len(chicken_pick)
for house in house_list:
    for i in range(len(chicken_pick)):
        val=1000
        for k in chicken_pick[i]:
           dist=cal_dist(house,k)
           val=min(val,dist)
        ans_arr[i]+=val 
            
print(min(ans_arr))