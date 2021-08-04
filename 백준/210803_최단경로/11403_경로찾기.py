import sys
read=sys.stdin.readline

# 3
# 0 1 0
# 0 0 1
# 1 0 0

N=int(read())
graph=[[]]
for _ in range(N):
    val_list=[0]+list(map(int,read().split()))
    graph.append(val_list)
result=[[0]*(N+1) for _ in range(N+1)]
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k]==0 or graph[k][j]==0:continue
            graph[i][j]=max(graph[i][j],graph[i][k]+graph[k][j])
     
# print(graph)
for i in range(1,len(graph)):
    for j in range(1,len(graph[i])):
        if graph[i][j]!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()