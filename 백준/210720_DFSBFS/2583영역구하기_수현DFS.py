import sys

sys.setrecursionlimit(10 ** 5)


def dfs(b, a):
    global count
    matrix[b][a] = 1
    for i in range(4):
        nx, ny = dx[i] + a, dy[i] + b
        if (0 <= ny < n) and (0 <= nx < m) and matrix[nx][ny] == 0:
            count += 1
            dfs(nx, ny)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []
count = 1
m, n, k = map(int, input().split())
matrix = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[j][i] = 1
for a in range(m):
    for b in range(n):
        if matrix[a][b] == 0:
            dfs(a, b)
            result.append(count)
            count = 1
result.sort()
print(len(result))
print(result)