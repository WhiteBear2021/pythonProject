import sys
from collections import deque
read=sys.stdin.readline
# 가로칸 M 세로칸 N
M,N=map(int,read().split())
# 익은 토마토 : 1, 익지않은토마토 : 0, 토마토가없을때 : 0 
totato_field=[list(map(int,read().split())) for _ in range(N)]

# print(totato_field)

# BFS 정의
queue=deque()
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS():
    while queue:
        print(queue)
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and totato_field[x][y] == 0:
                totato_field[x][y] = totato_field[a][b] + 1
                queue.append([x, y])
for i in range(N):
    for j in range(M):
        if totato_field[i][j] == 1:
            queue.append([i, j])
BFS()
result_YN = False
result = -2
                
for i in totato_field:
    for j in i:
        if j == 0:
            result_YN = True
        result = max(result, j)
if result_YN:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
    
# print(totato_field)