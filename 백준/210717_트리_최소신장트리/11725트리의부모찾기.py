import sys

# 최상위를 제외한 노드 갯수 N
N=int(sys.stdin.readline().strip())
node_arr=[0]*N
print(node_arr)
for i in range(len(node_arr)+1):
    if i!=0:
        