from collections import deque


def solution(board):
    answer = 0
    # matrix 배열
    matrix = board
    N=len(matrix)
    # 방문경로 배열
    visited = [[0 for col in range(N)] for row in range(N)]
    # 좌/우/위/아래 방향 이동
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # BFS 경로 탐색
    # queue 방식 사용
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 0
    print(matrix)
    d=-1
    while queue:
        val = queue.popleft()
        if len(val)==2:
            x,y=val[0],val[1]
        if len(val)==3:
            x,y,d=val[0],val[1],val[2]

        if x == N-1 and y == N-1:
            # 최종 경로 도착
            print(visited[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and matrix[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 100
                    queue.append((nx,ny,i))
                    if d!=-1:
                        if d!=i:
                            visited[nx][ny]+=500
    print(visited)
    return answer


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# board	result
# [[0,0,0],[0,0,0],[0,0,0]]	900
# [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	3800
# [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	2100
# [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	3200