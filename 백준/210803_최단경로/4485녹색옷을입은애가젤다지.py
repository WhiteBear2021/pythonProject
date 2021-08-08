import sys
import heapq
input=sys.stdin.readline
# INF=int(1e9)
INF=sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dijkstra(count):
    distance=[[INF]*N for _ in range(N)]
    q=[]
    # 처음에 0->0까지 arr[0][0] 처음 위치 비용 더하고 시작해야되니까 그 값으로 넣기
    heapq.heappush(q,[arr[0][0],0,0])
    distance[0][0]=arr[0][0]
    # q가 끝날때까지
    while q:
        cost,x,y=heapq.heappop(q)
        if x==N-1 and y==N-1:
            print(f"Problem {count}: {cost}")
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                ncost=cost+arr[nx][ny]
                if ncost<distance[nx][ny]:
                    distance[nx][ny]=ncost
                    heapq.heappush(q,[ncost,nx,ny])
cnt=1
while True:
    # NxN 배열
    N=int(input())
    # N값이 0이면 종료
    if N==0:break
    arr=[list(map(int,input().split())) for _ in range(N)]
    dijkstra(cnt)
    cnt+=1
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0