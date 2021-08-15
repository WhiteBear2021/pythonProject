import sys
input=sys.stdin.readline

# K 번
K=int(input())
result_list=[]
for _ in range(K):
    num=int(input())
    if num==0:
        result_list.pop()
    else:
        result_list.append(num)
        
print(sum(result_list))
