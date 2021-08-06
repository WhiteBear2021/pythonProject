import sys
from collections import deque
read=sys.stdin.readline
# DFS 정의
def dfs(graph,start,visited):
    global cnt
    visited[start]=True
    for node in graph[start]:
        if not visited[node]:
            cnt+=1
            dfs(graph,node,visited)
            

# 컴퓨터 수
N=int(read())
# 컴퓨터 연결된 쌍의 수
M=int(read())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)

visited_arr=[False]*(N+1)
cnt=0
dfs(graph,1,visited_arr)
print(cnt)
