# x,y,d,g 
# 출발지점 x,y, 시작방향, 세대
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
# 0 : (1,0) 1 : (0,-1) 2 : (-1,0) 3 : (0,1)

N=int(input())
map_list=[[0]*101 for _ in range(101)]
direction={0 : (1,0), 1 : (0,-1), 2 : (-1,0), 3 : (0,1)}
for _ in range(N):
    x,y,d,g=map(int,input().split())
    
    curves=[d]
    
    for _ in range(g):
        curves+=[(i+1)%4 for i in curves[::-1]]
    
    map_list[y][x]=1
    for curve in curves:
        x+=direction[curve][0]
        y+=direction[curve][1]
        map_list[y][x]=1
cnt=0
for i in range(100):
    for j in range(100):
        if map_list[i][j]+map_list[i+1][j]+map_list[i][j+1]+map_list[i+1][j+1]==4:
            cnt+=1
            
print(cnt)