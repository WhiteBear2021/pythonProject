# 테스트 케이스 횟수 T
T=int(input())

for _ in range(T):
    dic=dict()
# 테스트 케이스마다 옷의 갯수 N
    N=int(input())
    for _ in range(N):
        a,b=input().split()
        if dic.get(b):
            dic[b]+=1
        else:
            dic[b]=1
    # print(dic)
    sum=1
    for num in dic.values():
        sum*=(num+1)

    print(sum-1)
# 2
# 3
# hat headgear
# sunglasses eyewear
# turban headgear
# 3
# mask face
# sunglasses face
# makeup face