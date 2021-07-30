import sys
read=sys.stdin.readline

# 테스트 case 횟수 : T
T=int(read())
d=[0]*10001
d[1]=1
d[2]=2
d[3]=3
for i in range(4,10001):
    d[i]=d[i-1]+(d[i-2]-d[i-3])
    if i%3==0:
        d[i]+=1
# 테스트 케이스 횟수 만큼 반복문 돌고 값 출력
for t in range(T):
    # 답 구할 숫자 입력 받기
    num=int(read())
    print(d[num])
