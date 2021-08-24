import sys
input=sys.stdin.readline
# 부모노드 찾기 
def find_parent(parent,x):
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
# union_parent
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
# 컴퓨터 수 V
V=int(input())
# 선의 수 E
E=int(input())
# 비용순으로 오름차순 정렬할 연결된 컴퓨터 정보 담는 리스트 edges
edges=[]

# 부모노드 정보 가지고 있을 리스트
parent=[0]*(V+1)
for i in range(1,V+1):
    parent[i]=i
    
for _ in range(E):
    # 컴터 번호1 a, 컴터 번호2 b, 비용 c
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
    
# 비용순으로 오름차순 정렬
edges.sort()

# 최종 비용값 저장할 변수 result
result=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        result+=cost
        union_parent(parent,a,b)
        
print(result)

