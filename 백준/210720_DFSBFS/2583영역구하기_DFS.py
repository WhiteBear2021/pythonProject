import sys
from collections import deque
read=sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

# BFS 정의
def DFS(x,y):
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    rectangle_field[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and rectangle_field[nx][ny]==0:
            DFS(nx,ny)


def find_num_of_one(arr):
    one_cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                one_cnt+=1
                
    return one_cnt

N,M,K=map(int,read().split())
# 직사각형을 이루는 부분은 1, 아닌 부분을 0으로 할 배열 (N행 M열) 전체 0으로 생성
rectangle_field = [[0 for col in range(M)] for row in range(N)]

# 0 0을 기준으로 가까운 꼭지점 a,b 왼쪽, 제일 먼 꼭지점 x,y(이 숫자 전까지 표시되면 되는거)

for _ in range(K):
    a,b,x,y=map(int,read().split())
    for i in range(b,y):
        for j in range(a,x):
            rectangle_field[i][j]=1
    
# 영역 갯수 for문 돌면서 호출하는 DFS수만큼 cnt
cnt=0
# 영역의 넓이들을 배열에 담을 것이다. area_list (함수에서 처리)
area_list=[]
for i in range(N):
    for j in range(M):
        if rectangle_field[i][j]==0:
            # print(rectangle_field)
            sum1=find_num_of_one(rectangle_field)
            DFS(i,j)
            cnt+=1
            sum2=find_num_of_one(rectangle_field)
            area_list.append(sum2-sum1)
            # print(rectangle_field)
print(cnt)
area_list.sort()
for area in area_list:
    print(area,end=" ")