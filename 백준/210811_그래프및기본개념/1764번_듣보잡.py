import sys

# 듣도 못한 사람 수 N, 보도 못한 사람 수 M
N,M=map(int,input().split())

dic=dict()
for _ in range(N):
    name=input()
    dic[name]=1

answer_list=[]    
for _ in range(M):
    name=input()
    if dic.get(name):
        answer_list.append(name)

answer_list.sort()
print(len(answer_list))
for n in answer_list:
    print(n)        