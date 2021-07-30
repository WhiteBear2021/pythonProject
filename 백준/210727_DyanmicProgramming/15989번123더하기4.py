import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dp_topbottom(x):
    if x==1:return 1
    if x==2:return 2
    if x==3:return 3
    if d[x]!=0:
        return d[x]
    d[x]=dp_topbottom(x-1)+(dp_topbottom(x-2)-dp_topbottom(x-3))
    if x%3==0:
        d[x]+=1
    return d[x]
    
    
    
# 테스트 case 횟수 : T
T=int(read())

# 테스트 케이스 횟수 만큼 반복문 돌고 값 출력
for t in range(T):

    # 답 구할 숫자 입력 받기
    num=int(read())
    d=[0]*(num+1)
    d[1]=1
    d[2]=2
    d[3]=3
    print(dp_topbottom(num))
