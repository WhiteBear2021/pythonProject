import sys
input=sys.stdin.readline

# A의 집합 원소 갯수, B의 집합 원소 갯수
A,B=map(int,input().split())

list_A=list(map(int,input().split()))
list_B=list(map(int,input().split()))
set_AB=set(list_A+list_B)
num_AandB=A+B-len(set_AB)
# print(f"교집합 갯수 {num_AandB}")

# A의 차집합 갯수
result_A=A-num_AandB
# B의 차집합 갯수
result_B=B-num_AandB

print(result_A+result_B)