import sys, heapq
input=sys.stdin.readline
INF=int(1e9)

# 마을의 갯수 V, 도로의 갯수 E
V,E=map(int,input().split())
graph=[[INF]*(V+1) for i in range(V+1)]

distance=[INF]*(V+1)
graph=[[] for _ in range(V+1)]

for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(1)
# print(graph)
print(distance[V])