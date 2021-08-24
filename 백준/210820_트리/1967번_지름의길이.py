import sys
input=sys.stdin.readline
def find_parent(parent,x):
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드의 갯수 N
N=int(input())

# 부모노드 정보 가질 리스트 parent
parent=[0]*(N+1)
for i in range(1,N+1):
    parent[i]=i
    
# 모든 간선의 정보를 담을 리스트 edges 비용, 노드 a, 노드 b
edges=[]

# N-1개의 간선 정보입력 받는다 노드번호 a, 노드번호 b, 비용 c
for _ in range(N-1):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

# 비용 큰 순으로 내림차순 정렬
edges.sort(reverse=True)
print(edges)

# 비용 결과값 저장 변수 result
result=0

ans_list=[]
v_num=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        ans_list.append(edge)
        union_parent(parent,a,b)
        result+=cost
    else:
        v_num=find_parent(parent,a)
        break
print(parent)
print(v_num)
print(ans_list)
print(result)