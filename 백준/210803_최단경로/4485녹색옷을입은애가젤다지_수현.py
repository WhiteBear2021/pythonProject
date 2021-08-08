import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(n):
    M = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    dp = [[int(1e9)] * n for _ in range(n)]
    queue =[]
    heapq.heappush(queue,[M[0][0], 0, 0])
    dp[0][0] = M[0][0]
    while queue:
        m, x, y = heapq.heappop(queue)
        if x==n-1 and y==n-1:
            return m
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                new_dp=m+M[nx][ny]
                if new_dp<dp[nx][ny]:
                    dp[nx][ny] = new_dp
                    # print(dp)
                    heapq.heappush(queue, [new_dp, nx, ny])
    # print(dp)
    # return dp[n-1][n-1]
count = 0
while True:
    n = int(input())
    count+=1
    if n==0:
        break
    print(f"Problem {count}: {dfs(n)}")