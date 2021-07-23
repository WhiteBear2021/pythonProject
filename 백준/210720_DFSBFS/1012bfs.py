from collections import deque
import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)
# dfs 정의

def dfs(x,y):
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cabbage_field[x][y]=0
    q=deque()
    q.append([x,y])
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and cabbage_field[nx][ny]==1:
            dfs(nx,ny)
            


# Test케이스 갯수 T
T=int(read())


# print(T,M,N,K)


for _ in range(T):
# M : 가로, N : 세로, K:배추의 갯수
    M,N,K=map(int,read().split())
    # 배추밭을 이차원 배열로 표현
    cabbage_field = [[0 for col in range(M)] for row in range(N)]

# 배추밭있는 곳 1로 표현
    for _ in range(K):
        a,b=map(int,read().split())
        cabbage_field[b][a]=1
# 지렁이갯수 cnt 
    cnt=0
    for i in range(N):
        for j in range(M):
            if cabbage_field[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cabbage_field[x][y]=0
    queue=deque()
    queue.append([x,y])
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M and cabbage_field[nx][ny]==1:
                cabbage_field[nx][ny]=0
                queue.append([nx,ny])