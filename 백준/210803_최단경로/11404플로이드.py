# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

import sys
input=sys.stdin.readline

# 도시의 갯수 N, 버스의 갯수 M
N=int(input())

M=int(input())

# 버스의 도착도시, 드는 비용 값을 저장할 graph
#버스의 출발도시 도착도시 드는비용 순으로 값을 M번 받는다
graph=[[0 for col in range(N+1)] for row in range(N+1)]
for _ in range(M):
    start,arrive,cost=map(int,input().split())
    if graph[start][arrive]==0 or graph[start][arrive]>cost:
        graph[start][arrive]=cost
    
# print(graph)
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j or i==k or j==k:continue
            if graph[i][k]>0  and graph[k][j]>0:
                if graph[i][j]==0:
                    graph[i][j]=graph[i][k]+graph[k][j]
                else:
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# print(graph)
            
for i in range(1,len(graph)):
    for j in range(1,len(graph[i])):
        print(graph[i][j],end=" ")
    print()