import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)

# dfs 정의 (x,y) 위치를 인자로 받아서 정의
# 섬을 찾을 때 처음 1인 부분을 시작으로 (처음 1인 부분도 0으로 바꾸고 시작)
# 1인 부분이 땅이니까 상하좌우대각선까지 1인경우를 dfs로 확인 후 1인 부분을 0으로 바꿔준다 
# 상하좌우대각선 움직임 dx dy로 표현(상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
# 0인 부분이 나오면 dfs실행안하도록(1일 경우만 정의한 dfs 재귀적으로 호출해주면 된다)

def dfs(x,y):
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[-1,-1,0,1,1,1,0,-1]
    field[x][y]=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        print(nx,ny)
        if 0<=nx<h and 0<=ny<w:
            if field[nx][ny]==1:
                dfs(nx,ny)
    

# 필요한 값들 입력 받는 부분 정의 무한 루프 돌리고
# w와 h 값이 둘다 0을 받을 때 break
# 각 위치값이 섬인지(0) 땅인지(1) 여부 이차원 배렬로 받기
# 이차원 배열 for문 돌면서
while True:
    w,h=map(int,read().split())
    if w==0 and h==0:break
    field=[list(map(int, read().split())) for _ in range(h)]
    count=0
    for i in range(h):
        for j in range(w):
            if field[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)