import math

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

# 3
# 1.0 1.0
# 2.0 2.0
# 2.0 4.0
# print(math.dist((1.0,1.0), (2.0,2.0)))

# 별의 갯수
# N=int(input())
N=3
# stars 별들 정보 저장 (x좌표,y좌표) ex)3개면 0번별, 1번별, 2번별
stars=[(1.0,1.0),(2.0,2.0),(2.0,4.0)]
# for _ in range(N):
#     x,y=map(float,input().split())
#     stars.append((x,y))

# print(stars)

graph=[]
for i in range(N):
    for j in range(i+1,N):
        star_1=stars[i]
        star_2=stars[j]
        distance=math.dist(star_1,star_2)
        graph.append((distance,i,j))

graph.sort()
# print(graph)

# 부모노드를 저장할 리스트 parent
parent=[0]*(N)
# 부모노드를 자기자신으로 값을 초기화 해놓는다
for v in range(N):
    parent[v]=v

result=0
for g in graph:
    distance,i,j=g
    if find_parent(parent,i)!=find_parent(parent,j):
        result+=distance
        union_parent(parent,i,j)
        
print(round(result,2))
# print('%.2f' %ans)