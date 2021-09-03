from collections import deque
def bfs(p,r,c):
    # 상 하 좌 우로 움직일 때, x, y의 변화량
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    visited=[[False for a in range(5)] for b in range(5)]
    q=deque([])
    q.append((r,c,0))
    visited[r][c]=True
    while q:
        a,b,d=q.popleft()
        print(a,b,d)
        if d>2:continue
        if d!=0 and p[a][b]=="P":
            return False
        for i in range(4):
            nr=a+dx[i]
            nc=b+dy[i]
            if 0<=nr<=4 and 0<=nc<=4 and visited[nr][nc]==False:
                if p[nr][nc]=="X":continue
                visited[nr][nc]=True
                q.append((nr,nc,d+1))
    return True

def check(p):
    for i in range(5):
        for j in range(5):
            if p[i][j]=="P":
                if bfs(p,i,j)==False:
                    return False
    return True
def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


arr=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	
print(solution(arr))

# result=[1, 0, 1, 1, 1]