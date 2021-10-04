n,m,x,y,k = map(int,input().split())
map_ = [list(map(int,input().split())) for _ in range(n)]
ins = list(map(int,input().split()))
dice = [0,0,0,0,0,0]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in range(k):
    # print(i)
    d = ins[i]
    nx = x+dx[d]
    ny = y+dy[d]
    if not 0 <= nx < n or not 0 <= ny < m:
        continue
    if d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    if map_[nx][ny] == 0:
        map_[nx][ny] = dice[5]
    else:
        dice[5] = map_[nx][ny]
        map_[nx][ny] = 0
    x,y = nx,ny
    print(dice[0])