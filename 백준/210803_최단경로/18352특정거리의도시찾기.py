import sys, heapq
input=sys.stdin.readline
INF=int(1e9)
# 도시 수 N, 방향 수 M, 해당되는 거리 K, 시작하는 도시 X
N,M,K,X=map(int,input().split())
distance=[INF]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append((b,1))

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
                
dijkstra(X)
# print(distance)
check=False
# if K not in distance:
#     print(-1)
# else:
for i in range(1,len(distance)):
    if distance[i]==K:
        check=True
        print(i)
if check==False:
    print(-1)
