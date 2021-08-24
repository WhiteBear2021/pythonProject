import sys
input=sys.stdin.readline

# # of test case T
T=int(input())

for t in range(T):
    # 국가 수 N, 비행기 수 M
    N,M=map(int,input().split())
    # 연결된 비행기 정보
    airplane_graph=[[] for _ in range(N+1)]
    for m in range(M):
        # 두 도시 c d
        c,d=map(int,input().split())
        airplane_graph[c].append(d)
        airplane_graph[d].append(c)
    
    # 방문국가 check visited
    visited=[False]*(N+1)
    
    # 비행기 타는 횟수 cnt
    cnt=0
    for n in range(1,N+1):
        # 이미 방문한 국가이면 continue
        if visited[n]:
            continue
        # 방문한 국가가 아닐 경우 연결된 비행 수 만큼 cnt하고 방문처리
        
        
        