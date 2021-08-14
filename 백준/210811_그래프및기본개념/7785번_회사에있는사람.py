import sys, operator
input=sys.stdin.readline

# 로그 수 N
N=int(input())
# 출입 기록할 dictionary 자료구조
dic={}
for _ in range(N):
    # 이름 n, 출입상태(enter or leave) s
    n,s=input().split()
    if s=="leave":
        del dic[n]
    elif s=="enter":
        dic[n]=s

# dic=sorted(dic.items(), key=operator.itemgetter(0))
# print(dic)

for name in sorted(dic.keys(),reverse=True):
    print(name)
