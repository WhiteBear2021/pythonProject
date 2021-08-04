import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

# 정점의 갯수 N, 간선의 갯수 M
N,M=map(int,input().split())
# 시작 정점 번호 start
start=int(input())

graph=[[] for i in range(N+1)]
# idx값이 정점 번호라 생각하고 안에 들어있는 값은 시작점에서 정점까지 가는데 드는 비용을 넣을 것이다
# 초기값으로는 무한대 값을 설정해서 넣어놓는다
cost_arr=[INF]*(N+1)

for _ in range(M):
    # 시작정점번호, 끝정점번호, 정점까지의 비용
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q=[]
    # 자료구조 heap을 이용하여 q배열에 튜플로 (정점까지의비용,정점번호) 값 저장
    heapq.heappush(q,(0,start))
    # 처음 시작 노드에서는 비용이 0
    cost_arr[start]=0
    # q에 자료가 없어질때 까지
    while q:
        # q에 저장된 정정까지의 비용과 그 정점 번호를 꺼낸다
        now_cost,now_node=heapq.heappop(q)
        # cost배열에 저장된 비용이 점점까지의 비용보다 적으면 그냥 넘어간다 초기값은 INF로 설정되어있기때문에 무조건 저장된 값이 처음에는 클 것이다.
        if cost_arr[now_node]<now_cost:continue
        # 현재 정점에 연결된 노드 찾기 graph배열에 (정점번호,정점까지의 비용)
        for val in graph[now_node]:
            # val[0]가 정점번호인데 정점번호까지의 비용값 (val[1])을 그 전 노드까지의 비용값과 더해준다(now_cost)
            # adj_cost 은 즉 현재 있는 노드에서 인접한 노드까지 가는데 드는 비용값 구하기
            adj_cost=now_cost+val[1]
            # 만약 그 인접한 노드까지가는데 드는 비용이 원래 저장되어있는 cost_arr[인접한노드]보다 값이 적으면 갱신
            if adj_cost<cost_arr[val[0]]:
                cost_arr[val[0]]=adj_cost
                heapq.heappush(q,(adj_cost,val[0]))

dijkstra(start)
for i in range(1,N+1):
    if cost_arr[i]==INF:
        print("INF")
    else:
        print(cost_arr[i])
