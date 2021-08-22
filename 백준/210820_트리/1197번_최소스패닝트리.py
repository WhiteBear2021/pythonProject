import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
# 부모노드 찾는 함수(사이클이 되는지 안되는지 여부를 알기 위해)
def find_parent(parent,x):
    # 부모 노드가 자기 자신이 아니면 부모노드를 찾기
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x] #경로압축

def union_parent(parent,x,y):
    x=find_parent(parent,x)
    y=find_parent(parent,y)
    # 부모노드번호가 작은 번호를 부모 노드로 설정해주기
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

# 모든 간선 연결과 비용 정보를 담을 리스트 edges
edges=[]
# 최소스패닝트리 비용을 저장할 변수 result
result=0



# 정점의 갯수 V, 간선의 갯수 E
V,E=map(int,input().split())
# 부모노드를 저장할 리스트 parent
parent=[0]*(V+1)
# 부모노드를 자기자신으로 값을 초기화 해놓는다
for v in range(1,V+1):
    parent[v]=v
# 간선의 갯수 만큼 연결된 노드 a,b 비용 값을 받는다
for _ in range(E):
    a,b,cost=map(int,input().split())
    # 튜플 형태로 넣어주고 다 넣은 후 비용순으로 오름차순 정리(최소비용으로 만들기위해)
    edges.append((cost,a,b))

# 최소비용순으로 오름차순 정리
edges.sort()
# print(parent)
for edge in edges:
    cost,a,b=edge
    # 한번 방문한 것은 같은 부모를 가지도록 설정해놓기 때문에
    # 최소비용순으로 for문을 돌면서 부모노드가 다를 경우만 비용 계속 추가해준다
    # print(edge)
    # print(parent)
    if find_parent(parent,a)!=find_parent(parent,b):
        # 한번 지난것은 부모를 합쳐준다 (부모노드가 같아짐)
        result+=cost
        union_parent(parent,a,b)
        
print(result)