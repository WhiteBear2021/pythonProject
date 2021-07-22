import sys
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
list1 = [[row*col for col in range(1,N+1)] for row in range(1,N+1)]
# print(N,K,list1)

list2 = sum(list1, [])
list2.sort()
# print(list2)
print(list2[K])