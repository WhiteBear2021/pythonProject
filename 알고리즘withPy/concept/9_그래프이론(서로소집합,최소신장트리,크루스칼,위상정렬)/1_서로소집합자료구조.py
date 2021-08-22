# 1.find_parent(parent,x) 함수 구현
# : 특정 원소 x가 속한 집합을 알기 위해, 루트 노드를 찾기 위해 부모노드를 재귀적으로 호출
# 루트노드가 일치할 경우 : 서로소 집합이 아니다
def find_parent(parent,x):
    # 부모노드가 자기자신이면 그 노드번호가 루트노드일 것이다?
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    # 경로압축
    return parent[x]

# 2.union_parent(parent,a,b) 함수 구현
# :두개의 원소가 포함된 집합을 하나의 집합으로 합침(두 노드가 연결되어있을 때 더 작은 부모노드를 루트노드로 설정해주면서 집합을 만들어준다?)
def union_parent(parent,a,b):
    # a와 b의 부모노드를 찾는다
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    # 더작은 부모노드 번호를 루트노드로 설정
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
# 노드의 갯수 V, 간선의 수 E
V,E=map(int,input().split())
# 1~V번 모든 노드에 대한 부모노드를 담을 테이블
parent=[0]*(V+1)
# 1~V번 노드에 대해 자기자신으로 부모노드를 초기화 시켜놓는다
for i in range(1,V+1):
    parent[i]=i
# 연결된 간선의 노드의 부모노드를 각각 찾아주고 union_parent()함수를 통해 합쳐준다(부모노드를 작은번호으 부모노드로 통일시킴으로써)
for i in range(E):
    # 연결된 노드a, 노드b
    a,b=map(int,input().split())
    # 두 노드 합치기
    union_parent(parent,a,b)
    
# 각 원소가 속한 집합 출력
# 1~V번 각각의 노드의 최종 부모노드(즉, 루트노드를 출력)
print("각 노드의 부모노드 출력:")
for i in range(1,V+1):
    print(find_parent,(parent,i),end=" ")
print()

# 부모테이블의 내용 출력
for i in range(1,V+1):
    print(parent[i],end=" ")