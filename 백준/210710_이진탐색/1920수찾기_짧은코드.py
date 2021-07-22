import sys
n = sys.stdin.readline()
list_N = set(sys.stdin.readline().split())
m = sys.stdin.readline()
list_M = sys.stdin.readline().split()

for i in list_M:
    print(1) if i in list_N else print(0)
    
