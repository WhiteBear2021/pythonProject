import sys
N = int(sys.stdin.readline())
#번환해야할 행렬
m1 = list(map(int, list(input())))
m0 = list(m1)
#목표의 행렬
m2 = list(map(int, list(input())))

# print(m1)
# print(m2)
def change3(idx,m):
    for n in range(idx+1,idx-2,-1):
        if m[n]==0:
            m[n]=1
        else:
            m[n]=0
def change2(idx,m):
    for n in range(idx,idx-2,-1):
        if m[n]==0:
            m[n]=1
        else:
            m[n]=0
cnt=0
# 첫째 idx
change2(1,m1)
cnt+=1      
# 앞의 값 다르면 change
for i in range(1,N-1):
    if m1[i-1]!=m2[i-1]:
        change3(i,m1)
        cnt+=1
# 마지막값이 다르면 change
if m1[N-2]!=m2[N-2]:
    change2(N-1,m1)
    cnt+=1        
if m1==m2:
    print(cnt)
else:
    cnt=0
    for i in range(1,N-1):
        if m0[i-1]!=m2[i-1]:
            change3(i,m0)
            cnt+=1
    # 마지막값이 다르면 change
    if m0[N-2]!=m2[N-2]:
        change2(N-1,m0)
        cnt+=1
    if m0==m2:
        print(cnt)
    else:
        print(-1)  

