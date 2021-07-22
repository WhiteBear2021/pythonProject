import sys
# 주어진 숫자카드 갯수
N = int(sys.stdin.readline())
# 주어진 숫자카드 리스트
list_N = list(map(int, sys.stdin.readline().split()))
# 확인할 숫자카드 갯수
M = int(sys.stdin.readline())
# 확인할 숫자카드 리스트
list_M = list(map(int, sys.stdin.readline().split()))
# print(list_N)
# -10 -10 2 3 3 6 7 10 10 10

for i in list_M:
    print(1) if i in list_N else print(0)