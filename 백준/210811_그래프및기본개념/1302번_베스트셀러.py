import sys, operator
input=sys.stdin.readline

# 팔린 책의 갯수 N
N=int(input())
dic=dict()
for _ in range(N):
    # 구매한 책
    book=input()[:-1]
    if dic.get(book):
        dic[book]=dic[book]+1
    else:
        dic[book]=1
        
# print(dic)
dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(dic[0][0])
# print(dic)
# max_val=dic[0][1]
# for info in dic:
#     if info[1]!=max_val:
#         break
#     print(info[0])
# 5
# top
# top
# top
# top
# kimtop