import sys
from collections import deque
read=sys.stdin.readline
from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [list(map(int, read().strip())) for _ in range(N)]
# 방문경로 배열
visited = [[0 for col in range(M)] for row in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = deque()
queue.append([0,0])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
