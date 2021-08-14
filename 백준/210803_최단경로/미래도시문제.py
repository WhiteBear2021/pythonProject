import sys
input=sys.stdin.readline
INF=int(1e9)
# 회사 개수 N, 경로 개수 M
N,M=map(int,input().split())
graph=[[INF]*(N+1) for _ in range(N+1)]
# 연결된 회사 M개 값 받기
for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
# 방문해야하는 회사 X, 소개팅 회사 K
X,K=map(int,input().split())
for k in range(1,N+1):
    for a in range(1,K+1):
        for b in range(1,K+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
#출발회사에서 소개팅까지 중간까지 값
distance1=graph[1][K]    
print(distance1)
print(graph)
for x in range(1,N+1):
    for a in range(K,X+1):
        for b in range(K,X+1):
            graph[a][b]=min(graph[a][b],graph[a][x]+graph[x][b])
distance2=graph[K][X]
print(distance2)
print(graph)
print(distance1+distance2)
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 답 : 3