import sys
from collections import deque
read=sys.stdin.readline

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    cnt=0
    while queue:
        print(queue)
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt+=1
                visited[i]=True
    return cnt

# 컴퓨터 수
N=int(read())
# 컴퓨터 연결된 쌍의 수
M=int(read())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,read().split())
    graph[a].append(b)

visited_arr=[False]*(N+1)

print(bfs(graph,1,visited_arr))
print(visited_arr)