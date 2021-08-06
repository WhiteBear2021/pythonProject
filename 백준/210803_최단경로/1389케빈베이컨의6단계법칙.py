import sys
input=sys.stdin.readline

# 유저 수 N, 친구 관계 수 M
N,M=map(int,input().split())
# 친구 관계 표시할 그래프 관계 있을 경우 1로 표시
graph=[[0 for col in range(N+1)] for row in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
    
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if k==i or i==j or j==k:continue
            if graph[i][k]>0 and graph[k][j]>0:
                if graph[i][j]==0:
                    graph[i][j]=graph[i][k]+graph[k][j]
                else:
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                
result=int(1e9)
idx=0
for i in range(1,len(graph)):
    compr_sum=sum(graph[i])
    if 0<compr_sum<result:
        result=compr_sum
        idx=i
print(idx)

# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2