import sys
def changeAll(start_coord, arr):
    x, y = start_coord
    for i in range(x, x+3):
        for j in range(y, y+3):
            if arr[i][j]:
                arr[i][j]=False
            else:
                arr[i][j]=True    
                
N, M = map(int, sys.stdin.readline().split())
#번환해야할 행렬
m1 = [list(map(int, list(input()))) for _ in range(N)]
#목표의 행렬
m2 = [list(map(int, list(input()))) for _ in range(N)]
# print(m1)
# print(m2)
new_m=[]
cnt=0   #변경 횟수
for i in range(N):
    m=[0]*M
    for j in range(M):
        m[j]=m1[i][j]==m2[i][j]       
    new_m.append(m)
for i in range(N-2):
    for j in range(M-2):
        if not new_m[i][j]:
           changeAll((i,j),new_m) 
           cnt+=1
    if new_m[i][M-2]==False or new_m[i][M-1]==False:
        cnt=-1
        break
if sum(new_m[N-1])!=M or sum(new_m[N-2])!=M:
    cnt=-1
print(cnt)        
# print(new_m)
        
