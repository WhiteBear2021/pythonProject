import sys
from collections import deque
read=sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
# BFS 정의
def BFS(x,y):
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    q.append([x,y])
    rectangle_field[x][y]=1
    area_rectangle=1
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M and rectangle_field[nx][ny]==0:
                area_rectangle+=1                  
                rectangle_field[nx][ny]=1
                q.append([nx,ny])
    area_list.append(area_rectangle)


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
            print(rectangle_field)
            BFS(i,j)
            cnt+=1
            print(rectangle_field)
            
print(cnt)
area_list.sort()
for area in area_list:
    print(area,end=" ")