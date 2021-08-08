from heapq import heappush, heappop
import sys

INF = sys.maxsize
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dij(cnt):
    d, q = [[INF]*n for _ in range(n)], []
    heappush(q, [a[0][0], 0, 0])
    d[0][0] = a[0][0]
    while q:
        w, x, y = heappop(q)
        if x == n-1 and y == n-1:
            print("Problem {0}: {1}".format(cnt, w))
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                nw = w + a[nx][ny]
                if nw < d[nx][ny]:
                    d[nx][ny] = nw
                    heappush(q, [nw, nx, ny])

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    dij(cnt)
    cnt += 1