import sys
from collections import deque

# DFS 정의
def dfs(graph,start,visited):
    visited[start]=True
    print(start,end=" ")
    graph[start].sort()
    for node in graph[start]:
        if not visited[node]:
            dfs(graph,node,visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                
            
            
# 노드 갯수 N, 간선 갯수 M, 시작 점 V
N,M,V =map(int, sys.stdin.readline().split())

visited_arr=[False]*(N+1)

arr=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited_arr2=[False]*(N+1)
arr2=arr[0:]

dfs(arr,V,visited_arr)

print()

bfs(arr2,V,visited_arr2)