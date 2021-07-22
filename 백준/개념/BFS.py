from collections import deque
import sys

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
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
    
    
bfs(arr,V,visited_arr)