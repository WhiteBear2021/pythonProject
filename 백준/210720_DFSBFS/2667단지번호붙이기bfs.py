import sys
from collections import deque
read=sys.stdin.readline
sys.setrecursionlimit(100000)

# dfs정의
def bfs(x,y):
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append([x,y])
    village_field[x][y]=0
    while queue:
        a,b=queue.popleft()  
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and village_field[nx][ny]==1:
                village_field[nx][ny]=0
                queue.append([nx,ny])
        
def find_num_of_one(arr):
    one_cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                one_cnt+=1
                
    return one_cnt

# 길이가 N인 정사각형
N=int(read())
village_field=[list(map(int, read().strip())) for _ in range(N)]
village_cnt=0
building_cnt_arr=[]
for i in range(N):
    for j in range(N):
        if village_field[i][j]==1:
            village_cnt+=1
            sum1=find_num_of_one(village_field)
            bfs(i,j)
            sum2=find_num_of_one(village_field)
            building_cnt_arr.append(sum1-sum2)
            
building_cnt_arr.sort()
print(village_cnt)
for building_cnt in building_cnt_arr:
    print(building_cnt)