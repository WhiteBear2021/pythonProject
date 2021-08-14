from collections import deque

T = int(input())
dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(T):
    l = int(input())
    m = [[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int , input().split())
    queue = deque()
    queue.append([sx,sy])
    while queue:
        x, y = queue.popleft()
        # print(f"x,y값 : {x},{y}")
        if x==ex and y==ey:
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and m[nx][ny]==0:
                queue.append([nx, ny])
                m[nx][ny] = m[x][y]+1
    # print(m)
    print(m[ex][ey])