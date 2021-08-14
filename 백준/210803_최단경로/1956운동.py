import sys
input=sys.stdin.readline
INF=int(1e9)

# 마을의 갯수 V, 도로의 갯수 E
V,E=map(int,input().split())
graph=[[INF]*(V+1) for i in range(V+1)]

# for a in range(1,V+1):
#     for b in range(1,V+1):
#         if a==b:
#             graph[a][b]=0

for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a][b]=c
sum=INF
for i in range(1,V+1):
    if graph[i][i]!=INF:
        sum=min(sum,graph[i][i])
if sum!=INF:
    print(sum)
else:
    for k in range(1,V+1):
        for a in range(1,V+1):
            for b in range(1,V+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

    for a in range(1,V+1):
        for b in range(1,V+1):
            if graph[a][b]+graph[b][a]<sum:
                sum=graph[a][b]+graph[b][a] 

    # print(graph)
    if sum==INF:
        print(-1)
    else:
        print(sum)