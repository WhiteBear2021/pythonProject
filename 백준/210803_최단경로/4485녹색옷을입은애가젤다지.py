import sys
input=sys.stdin.readline

while True:
    # NxN 배열
    N=int(input())
    # N값이 0이면 종료
    if N==0:break
    graph=[list(map(int,input().split())) for _ in range(N)]
    
    print(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i==j or i==k or j==k:continue
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                
    print(graph)