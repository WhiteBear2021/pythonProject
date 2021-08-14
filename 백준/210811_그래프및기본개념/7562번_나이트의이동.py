import sys
from collections import deque
read=sys.stdin.readline

# BFS 정의
def BFS(x,y):
    # 상하좌우
    dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
    q=deque()
    q.append([x,y])
    while q:
        a,b=q.popleft()
        for i in range(8):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<I and 0<=ny<I and chess_field[nx][ny]==0:
                q.append([nx,ny])
                chess_field[nx][ny]=chess_field[a][b]+1
            if nx==x2 and ny==y2:
                return


# 테스트 케이스 횟수 N
N=int(input())
# result_arr
result_arr=[]
for _ in range(N):
    # IxI의 체스판 I 값 받기
    I=int(input())
    chess_field=[[0]*I for _ in range(I)]
    # print(chess_field)
    # 시작 좌표 값 받기
    x1,y1=map(int,input().split())
    # 도착 좌표 값 받기
    x2,y2=map(int,input().split())
    if x1==x2 and y1==y2:
        print(0)
    else:
        BFS(x1,y1)
        print(chess_field[x2][y2])
    


# 2
# 4
# 0 0
# 0 0
# 4
# 1 1
# 1 1