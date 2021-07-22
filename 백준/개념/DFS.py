import sys

# DFS 정의
def dfs(graph,start,visited):
    visited[start]=True
    print(start,end=" ")
    graph[start].sort()
    for node in graph[start]:
        if not visited[node]:
            dfs(graph,node,visited)
            
# 노드 갯수 N, 간선 갯수 M, 시작 점 V
N,M,V =map(int, sys.stdin.readline().split())

visited_arr=[False]*(N+1)

arr=[[] for _ in range(N+1)]
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(arr,V,visited_arr)