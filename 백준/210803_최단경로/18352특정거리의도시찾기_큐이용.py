import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[x] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == INF:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

for i in range(n+1):
    if distance[i] == k:
        print(i)

if k not in distance:
    print(-1)