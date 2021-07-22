import sys

# DFS 정의
def dfs(graph,start,visited):
    visited[start]=True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph,node,visited)

# 노드 갯수 N, 간선 갯수 M
N,M =map(int, sys.stdin.readline().split())

visited_arr=[False]*(N+1)

arr=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

cnt=0    
for j in range(1,N+1):
    if not visited_arr[j]:
        cnt+=1
        dfs(arr,j,visited_arr)
        
print(cnt)