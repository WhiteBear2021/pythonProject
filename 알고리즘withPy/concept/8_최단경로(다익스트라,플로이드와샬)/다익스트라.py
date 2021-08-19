import sys
input=sys.stdin.readline
INF=int(1e9)  #무한을 의미하는 10억
# 노드의 갯수 N, 노드간 연결된 간선의 갯수 M
N,M=map(int,input().split())
#시작 노드 번호 1
start=1 
# 노드 방문여부 정보 담기
visited=[False]*(N+1)
# 최소거리비용을 저장할 리스트
distance=[INF]*(N+1)

# 노드 연결정보 담기 graph[기준노드번호]=(연결된노드번호,비용)으로 담을 것이다
graph=[[] for i in range(N+1)]

for i in range(M):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
# 방문하지 않은 노드 중 가장 거리가 짧은 노드 번호를 제공할 함수
def get_smallest_node():
  min_value=INF
  index=0
  for i in range(1,N+1):
    if distance[i]<min_value and not visited[i]:
      min_value=distance[i]
      index=i
  return index

# 다익스트라 최단경로 알고리즘 구현
def dijkstra(start):
  # 시작지점 거리 비용을 0, 방문 True 설정
  distance[start]=0
  visited[start]=True
  # 시작지점에서 연결된 노드와 비용을 통해 distance 비용 값 갱신해준다 INF->비용으로 바뀔 것이다
  # graph[노드번호]=(연결된노드,비용)이 들어있으므로 j가 (연결된노드,비용)을 나타낸다
  for j in graph[start]:
    distance[j[0]]=j[1]
  # 시작 녿 빼고 n-1개 노드에 대한 반복?
  for i in range(N-1):
    # 방문하지 않은 노드 중에 최단거리가 짧은 노드 꺼내기. 그다음 방문처리.
    now=get_smallest_node()
    visited[now]=True
    # 꺼낸 노드에서 연결된 다른 노드를 확인
    for j in graph[now]:
      cost=distance[now]+j[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 비용 distance값 갱신
      if cost<distance[j[0]]:
        distance[j[0]]=cost
# 다익스트라 알고리즘 호출 수행
dijkstra(start)

# 모든 노드를 가는데 드는 최소 비용 출력
for i in range(1,N+1):
  # 도달할 수 없는 경우 INF값을 가지고 있을 것이다
  if distance[i]==INF:
    print("Infinity")
  else:
    print(distance[i])